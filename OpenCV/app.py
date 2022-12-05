from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
def gen_frames(camera):
    while True:
        ret, frame = camera.getFrame()
        if ret:
            yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            break
               
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
