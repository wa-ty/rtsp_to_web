# rstp_to_web
For viewing RTSP feeds in your web browser really easy. Run this on a network with IP cameras attached and process the rtsp footage live into mp4 streams.

# How it works

Using opencv with ffmpmeg allows you to stream rtsp format video using the standard `cv2.VideoCapture` class.

A Queue is used to provide thread-safe frames to be grabbed by the client (read [here](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues)).

Currently each client will spin up a thread for each video, so I'd assume a lot of clients might fry the flask process.



# One Feed

<img src="images/one.png">

```python
ips = [
  'rtsp://admin:123456@192.168.1.101:554/h264'
]
```

# Multiple Feeds

<img src="images/five.png">

```python
ips = [
  'rtsp://admin:123456@192.168.1.101:554/h264',
  'rtsp://admin:123456@192.168.1.101:554/h264'
  'rtsp://admin:123456@192.168.1.101:554/h264'
  'rtsp://admin:123456@192.168.1.101:554/h264'
  'rtsp://admin:123456@192.168.1.101:554/h264'
]
```


