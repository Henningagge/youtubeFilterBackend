
from recomendations import loadVidoeRecomendations
from Playlists import getPlaylistViaChannelId, openPlaylist
from topicSwap import  switchTopic
#! a flash server with my own api where i can then make request

from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def servermain():
    return "Hello from Server"


@app.route("/recomendations")
def loadRecomendationsApi():
    result = loadVidoeRecomendations("UCsd4OmYbE6BeYEdm-Vn7pcQ")
    return result
@app.route("/swap")
def swapTopicApi():
    switchTopic()


@app.route("/playlists")
def loadPlaylistsApi():
    result = getPlaylistViaChannelId()
    return result

@app.route("/openPlaylist/{id}")
def openPlaylistApi():
    result = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")
    return result

if __name__ == "__main__":
    app.run()


