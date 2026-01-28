
from recomendations import loadVidoeRecomendations
from playlists import getPlaylistViaChannelId, openPlaylist
from topicSwap import  switchTopic
from flask_cors import CORS, cross_origin

from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def servermain():
    return "Hello from Server"


@app.route("/recomendations")
def loadRecomendationsApi():
    result = loadVidoeRecomendations()
    return result

@app.route("/swap")
def swapTopicApi():
    switchTopic("UCsd4OmYbE6BeYEdm-Vn7pcQ")


@app.route("/playlists")
def loadPlaylistsApi():
    result = getPlaylistViaChannelId()
    return result

@app.route("/openPlaylist")
def openPlaylistApi():
    result = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")
    return result

if __name__ == "__main__":
    app.run()


