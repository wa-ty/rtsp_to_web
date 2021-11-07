from flask import Flask, render_template, Response, request
import config
import math
import stream

app = Flask(__name__)

@app.route('/')
def index():
  num_ips = len(config.ips)
  scale = 100 / math.ceil(math.sqrt(num_ips))
  return render_template('index.html', ips=config.ips, scale=scale)

@app.route('/video_feed')
def video_feed():
  link = request.args['link']
  return Response(stream.gen_frames(link), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
