import cv2
class VideoCamera(object):
    def __init__(self):
      self.video = cv2.VideoCapture(cv2.CAP_V4L2)
      self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
      self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
      if self.video.isOpened():
        print("Camera Connected..")
      else:
        print("Camera is not connected..")

    def __del__(self):
      self.video.release()
      print("Video released")

    def getFrame(self):
      success, frame = self.video.read()
      if not success:
        return success, 0
      else:
        ret, jpeg = cv2.imencode('.jpg', frame)
        return ret, jpeg.tobytes()
