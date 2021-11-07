Every way to do this online sucks

## How it works

Using opencv with ffmpmeg allows you to stream rtsp format video using the standard `cv2.VideoCapture` class.

Due to synchronization issues, a Queue is used to provide thread-safe frames to be grabbed by the client (read [here](https://docs.python.org/3/library/multiprocessing.html#pipes-and-queues)).

One stream will be created for each rtsp stream provided. These streams will be set as the source on the flask index page.

## Settings

The file `config.py` contains a list of ips that will all be loaded into the web page.
