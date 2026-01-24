import os
from constants import  Api_Key
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import unittest
from variable import currentTopicChannelId
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
            part="snippet",
            channelId=currentTopicChannelId,
        )
        response = request.execute()
    except Exception as e:
        print(f"There has been an error when requesting the Youtube Api for the Playlists of a Channel error: {e}")
        return []

    playlistRecource = {}
    
    for item in response["items"]:
        playlistRecource[item["id"]] = item["snippet"]["title"]
        playlistRecource[item["id"]] = [playlistRecource[item["id"]], item["snippet"]["thumbnails"]["default"]["url"]   ]
        #? has a width of 120 and height if 90   other options than default if medium w:320 h:180
        
    return playlistRecource

def getVideosinPlaylist(playlistId):
    api_service_name = "youtube"
    api_version = "v3"
    try:
        youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
        request = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlistId
        )
        response = request.execute()               #! diese function ist noch nicht fertig  werden und tests sind auch noch nicht da
    except Exception as e:
        print(f"There has been an error when requesting the videos of a Playlist via it's id error:  {e}")
        return []

    videos = []

    for item in response["items"]:
        videos.append(item["contentDetails"].get("videoId"))

    return videos




def openPlaylists(playlistid):
    pass



def sendPlayliststoFrontend(playlistids):
    pass

#diese funktionalität ist verschoben weil man oAuth2 braucht undheute kein bock
#todo wie sieht das eigentlich auß brauch ich für mehrer kanäle dann immer anderes oAuth2 oder nicht?
def insertIntoPlaylist(playlistid, videoid):
    pass
    

def deleteOutofPlaylist(playlistid, videoid):
    pass






