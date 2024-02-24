from pytube import YouTube

def youtube(URL):
  # URL = unquote(request.args.get("url"))

  # Initializing the downloader
  yt = YouTube(URL)
  streams = yt.streams.asc()
  
  obj = { "with_audio": [], "without_audio": [], "only_audio": [], "video_info": {} }
  
  first_stream = streams[0]
  obj["video_info"]["title"] = first_stream.title
  
  for stream_obj in streams:
    stream_type = stream_obj.type
    custom_streams = { "type": stream_type, "subtype": stream_obj.subtype, "url": stream_obj.url }
    # calculating the size of the video
    filesize_kb = stream_obj.filesize_kb
    if filesize_kb > 1000:
      filesize_mb = stream_obj.filesize_mb
      if filesize_mb > 1000:
        custom_streams["size"] = str(stream_obj.filesize_gb) + "GB"
      else:
        custom_streams["size"] = str(filesize_mb) + "MB"
    else:
      custom_streams["size"] = str(filesize_kb) + "KB"
    # categorizing the videos
    if stream_type == "video":
      custom_streams["fps"] = stream_obj.fps
      custom_streams["resolution"] = stream_obj.resolution
    if stream_type == "video":
      obj["with_audio" if stream_obj.is_progressive == True else "without_audio"].append(custom_streams)
    else:
      obj["only_audio"].append(custom_streams)
  return jsonify(obj)
