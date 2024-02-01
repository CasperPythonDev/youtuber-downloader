from pytube import YouTube
from pathlib import Path  # TODO

# TODO Implement progres bar while downloading
# TODO Implement TK Interface


def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        higest_res_stream = streams.get_highest_resolution()
        higest_res_stream.download(output_path=save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print(e)


video_url = "https://www.youtube.com/watch?v=U6u39w60iwI"
save_path = "./"  # TODO use pathlib object

download_video(video_url, save_path)  # TODO first test shows 720p download
