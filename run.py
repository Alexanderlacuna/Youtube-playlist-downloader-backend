from flask import Flask ,jsonify,request

# from test import saveVideo,downloadPlaylist
from test import *


from flask_cors import CORS



app=Flask(__name__)

CORSz(app)

# routes
# dowload specific video:

@app.route("/getVideoDetails")
def details():
	return "EW"

@app.route("/home")
def home():
	return "home"

# @app.route("/dowloadVideos/<path:url>")
# def download(url):

# 	print(url)


	# myUrl="https://www.youtube.com/playlist?list=PL4cUxeGkcC9jLYyp2Aoh6hcWuxFDX6PBJ"
# 	# downloadPlaylist(myUrl)

# 	return "dwe"

# util methods

def download(url):
	saveVideo(url)

@app.route("/playlist",methods=["POST"])
def allPlaylist():
	data=request.get_json()

	try:
		playlistUrl=data["url"]

		print(playlistUrl)

		response=downloadPlaylist(playlistUrl)

	except Exception as e:
		raise e


	return response


if __name__ == '__main__':
	app.run(debug=True)