import bs4
from urllib.request import urlopen  as uReq
from bs4 import BeautifulSoup as soup
from pytube import YouTube
import os
import multiprocessing

from flask import jsonify




videoList=[]

def getDetails(video):
	detail={}
	print(video)
	link=f'https://youtube.com{video["href"]}'
	yt=YouTube(link)
	print(yt)
	# print(yt)
	# detail["description"]=yt.description
	detail["length"]=int(yt.length/60)
	detail["img"]=yt.thumbnail_url
	detail["views"]=yt.views
	detail["title"]=yt.title
	details["link"]=link


	# return detail

	return detail


def getVideo():
	vidos=[]
	try:
		for video in videoList:

			v=getDetails(video)
			vidos.append(v)


	except Exception as e:
		return jsonify({"message":str(e)}),401

	return jsonify({"videos":vidos})


	



def saveVideo(url,path=""):
	print("working")
	yt=YouTube(url)
	videoDetails=getDetails(yt)
	yt.streams.filter(progressive=True,file_extension="mp4").order_by("resolution").desc().first().download(path)


	print(f"finished dowloading {yt.title}")







def downloadPlaylist(playlistUrl):
	try:
		uClient=uReq(playlistUrl)
		page=uClient.read()
		uClient.close()

		page_soup=soup(page,"html.parser")
		# videos=page_soup.findAll("a",{"class":"pl-video-title-link"})
		videos=page_soup.findAll("a",{"class":"pl-video-title-link"})

		# print(len(videos))

		# videoList.append(videos)
		newList=[]

		for video in videos:
			link=f'https://youtube.com{video["href"]}'
			print(link)
			# path="C:\Users\alex\Downloads"
			# path=os.path.abspath("C:/Users/alex/Downloads")
			# print(path)
			# saveVideo(link)
			x=getDetails(video)
			print(x)
			newList.append(x)



			# prc=multiprocessing.Process(target=saveVideo,args=(link,))
			# prc.start()
			# prc.join()



	except Exception as e:
		return jsonify({"message":str(e)}),401


	return(jsonify({"videos":newList}))

	print("finished playlist")




