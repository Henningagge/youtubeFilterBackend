
from recomendations import loadVidoeRecomendations
from playlists import getPlaylistViaChannelId, openPlaylist
from topicSwap import switchTopic
from flask_cors import CORS, cross_origin

from flask import Flask

app = Flask(__name__)
cors = CORS(app)


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
    response = getPlaylistViaChannelId()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/openPlaylist")
def openPlaylistApi():
    response = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("getTopics")
def getTopics():
    response = getChannelTopics()
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
if __name__ == "__main__":
    app.run()
