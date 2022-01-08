#!/usr/bin/python3

import pytube
from pytube import YouTube
# By E4crypt3d

def downloadVideo():
	URL = input("Paste the URL of the video: ")
	if type(URL) == str:
		yt = YouTube(URL)																										
		video = yt.streams.filter(resolution='720p').first()
		print("Video Title: == ",video.title)
		print("Video Size: == ",video.filesize)
		savepath = input("Please specify the directory you want to save the video: ")
		if type(savepath) == str:
			video.download(savepath)
			print(video)
			print("Video downloaded successfuly")
		else: 
			print("Please enter a vaid path")
			downloadVideo()

	else:
		print("Please enter a valid URL")
		downloadVideo()

downloadVideo()
