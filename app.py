from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def index():
  return "<h1>Hello, this is a home page!</h1>"

@app.get("/yt")
def yt():
  # required modules ko import kiya ja raha hai
  from pytube import YouTube
  from urllib.parse import unquote

  url = request.args.get("url")

  if not url: return "URL is required!"
  
  url = unquote(url)

  try:
    yt = YouTube(url)
    streams = yt.streams
    audio_streams = []
    video_streams = []

    methods = [ 'abr', 'audio_codec', 'bitrate', 'codecs', 'default_filename', 'expiration', 'filesize', 'filesize_approx', 'filesize_gb', 'filesize_kb', 'filesize_mb', 'includes_audio_track', 'includes_video_track', 'is_3d', 'is_adaptive', 'is_dash', 'is_hdr', 'is_live', 'is_otf', 'is_progressive', 'itag', 'mime_type', 'resolution', 'subtype', 'title', 'type', 'url', 'video_codec' ]

    for stream in streams.filter(only_audio=True):
      audio_data = { method: getattr(stream, method) for method in methods }
      audio_streams.append(audio_data)

    methods.insert(11, "fps")

    for stream in streams.filter(only_video=True):
      video_data = { method: getattr(stream, method) for method in methods }
      video_streams.append(video_data)

    return jsonify({ "videos": video_streams, "audios": audio_streams })
  except Exception as e:
    print(e)
    return str(e)

if __name__ == "__main__":
  """
  import sys
  from gunicorn.app.wsgiapp import run
  sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
  sys.exit(run())
  """
  app.run(debug=True)