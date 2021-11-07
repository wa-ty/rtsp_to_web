For viewing RTSP feeds in your web browser really easy

## How it works

Using opencv with ffmpmeg allows you to stream rtsp format video using the standard `cv2.VideoCapture` class.

A Queue is used to provide thread-safe frames to be grabbed by the client (read [here](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues)).

Currently each client will spin up a thread for each video, so I'd assume a lot of clients might fry the flask process.

## Settings

The file `config.py` contains a list of ips that will all be loaded into the web page.
