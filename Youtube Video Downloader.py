# Download any video from youtube

# Importing Libraries
from pytube import *

# Getting Video Link
video = input("Enter URL of Video: ")
video_link = YouTube(video).streams

i = 1


for stream in video_link:
    try:
        print(str(i) + ". " + str(stream))
        if i == 10:
            break
        i += 1
    except DeprecationWarning:
        pass


stream_number = int(input("Enter Number: "))

video = video_link[stream_number]
video.download("C:'\'Users'\'user'\'Desktop")

print("Downloaded")