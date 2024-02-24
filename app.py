from flask import Flask, request, jsonify
from urllib.parse import unquote

from modules import *

app = Flask(__name__)

# Home page
@app.get("/")
def index():
  return "<h1>Hello, this is a home page!</h1>"

# Ye code YouTube kee videos kee information deta hai
@app.get("/yt")
def yt():
  return youtube(unquote(request.args.get("url")))
