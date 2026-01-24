import os
from constants import  Api_Key
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import unittest
from variable import currentTopicChannelId
from recomendations import getChannelRecource, getVideoLength
api_service_name = "youtube"
api_version = "v3"

def getPlaylistViaChannelId():
    """
    Docstring for getPlaylistViaChannelId   

    returns a list of playlist ids
    """
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
    videoIds = getVideosinPlaylist(playlistid)
    videoRecources = []
    for videoId in videoIds:
        vidoeRecource = getVideoRecourse(videoId)
        videoRecources.append(vidoeRecource)
    sendPlayliststoFrontend(videoRecources)

        


def getVideoRecourse(videoId):
    videoRecource = {}
    youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
    videoLength = getVideoLength(videoId)   
    videoRecource[videoId] = videoLength
    request = youtube.videos().list(
                part="snippet",
                id = videoId
            )
    response = request.execute() 
    videoTitle = response["items"][0]["snippet"]["title"]
    channelid = response["items"][0]["snippet"]["channelId"]
    vidoeThumbnail = response["items"][0]["snippet"]["thumbnails"]["default"]["url"]
    channelRecource = getChannelRecource(channelid)
    #Duration, title, ThumbnailUrl, ChannelId, channelName, ChannelBanner
    videoRecource[videoId] = [videoRecource[videoId], videoTitle,  vidoeThumbnail, channelid, channelRecource[1], channelRecource[2]]

    return videoRecource




def sendPlayliststoFrontend(videoRecources):
    pass

#diese funktionalität ist verschoben weil man oAuth2 braucht undheute kein bock
#todo wie sieht das eigentlich auß brauch ich für mehrer kanäle dann immer anderes oAuth2 oder nicht?
def insertIntoPlaylist(playlistid, videoid):
    pass
    

def deleteOutofPlaylist(playlistid, videoid):
    pass






