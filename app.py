from flask import Flask

app = Flask(__name__)

@app.get("/")
def index():
  return "<h1>Hello, this is a home page!</h1>"

@app.get("/yt")
def yt():
  import pytube

if __name__ == "__main__":
  import sys
  from gunicorn.app.wsgiapp import run
  sys.argv = "gunicorn --bind 0.0.0.0:5151 app:app".split()
  sys.exit(run())
