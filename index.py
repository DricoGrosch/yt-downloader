from pytube import YouTube
from moviepy.editor import *

url = str(input("Enter the URL of the video you want to download: \n>>"))
yt_video = YouTube(url)
stream = yt_video.streams.get_highest_resolution()
downloaded_file = stream.download()
video = VideoFileClip(downloaded_file)
audio = video.audio
audio.write_audiofile(f'{yt_video.title}.mp3')