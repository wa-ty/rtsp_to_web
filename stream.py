import cv2, queue, threading
from datetime import datetime, timedelta

class VideoCapture:
  def __init__(self, name):
    self.cap = cv2.VideoCapture(name)
    self.q = queue.Queue()
    self.last_interaction = datetime.now()
    t = threading.Thread(target=self.worker)
    t.daemon = True
    t.start()

  def worker(self):
    while True:
      ret, frame = self.cap.read()
      if not ret:
        break
      if not self.q.empty():
        try:
          self.q.get_nowait()
        except queue.Queue.Empty:
          pass
      self.q.put(frame)

  def read(self):
    self.last_interaction = datetime.now()
    return self.q.get()


def gen_frames(link):
  cap = VideoCapture(link)
  while True:
    print('running')
    if timedelta(seconds=5) < (datetime.now() - cap.last_interaction):
      print('killing')
      break
    frame = cap.read()
    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')