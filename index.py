from pytube import YouTube
from moviepy.editor import *
import os
url = str(input("Enter the URL of the video you want to download: \n>>"))
yt_video = YouTube(url)
stream = yt_video.streams.get_highest_resolution()
downloaded_file = stream.download('media')
video = VideoFileClip(downloaded_file)
audio = video.audio
audio.write_audiofile(f'./media/{yt_video.title}.mp3')