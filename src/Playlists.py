import os
from constants import currentTopicChannelId, Api_Key
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def getPlaylistViaChannelId():
    """
    Docstring for getPlaylistViaChannelId   

    returns a list of playlist ids
    """
    api_service_name = "youtube"
    api_version = "v3"
    try:
        youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
        request = youtube.playlists().list(
            part="contentDetails",
            channelId=currentTopicChannelId,
        )
        response = request.execute()
    except Exception as e:
        print(f"There has been an error when requesting the Youtube Api for the Playlists of a Channel error: {e}")
        return []

    playlistIds = []
    for item in response["items"]:
        playlistIds.append(item["id"])
    return playlistIds




def insertIntoPlaylist(playlistid, videoid):
    pass

def deleteOutofPlaylist(playlistid, videoid):
    pass





#youtube api für die zwei unteren funktionen
#insert


#delete

