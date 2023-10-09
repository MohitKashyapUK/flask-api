from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def index():
  return "<h1>Hello, this is a home page!</h1>"

@app.get("/yt")
def yt():
  from pytube import YouTube
  from urllib.parse import unquote
  url = request.args.get("url")
  if not url:
    return "URL is required!"
  else:
    url = unquote(url)
  try:
    yt = YouTube(url)
    streams = yt.streams
    video_streams = streams.filter(progressive=False, only_video=True)
    # audio_streams = streams.filter(progressive=False, only_audio=True)
    methods = [ method for method in dir(video_streams) if not method.startswith("_") ]
    json_data = {}
    for method in methods:
      prop = getattr(video_streams, method)
      if not callable(prop):
        json_data[method] = prop
    return jsonify(json_data)
  except Exception as e:
    return "Something went wrong!"

if __name__ == "__main__":
  import sys
  from gunicorn.app.wsgiapp import run
  sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
  sys.exit(run())
