import random 
from constants import  Api_Key
import googleapiclient.discovery
import re
from variable import currentTopicChannelId
api_service_name = "youtube"
api_version = "v3"


def getSubscribedChannels(userChannelId):
    youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
    request = youtube.subscriptions().list(
                part="snippet",
                channelId = userChannelId
            )
    try:
        response = request.execute() 
    except Exception as e:
        print(f"Error when trying to get Channel Recource error: {e}")

    channelIds = []
    for item in response["items"]:
        channelIds.append(item["snippet"]["resourceId"]["channelId"])

    return channelIds


def getVideosofChannels(channelsidarr):
    videosIds = []
    youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
    for chanid in channelsidarr:
        request = youtube.search().list(
                    part="snippet",
                    channelId=chanid,
                    maxResults=2,
                    order="date",
                    type="video"
                )
        try:
            response = request.execute() 
        except Exception as e:
            print(f"Error when trying to get Channel Recource error: {e}")
        for item in response["items"]:
            videosIds.append(item["id"]["videoId"])
    return videosIds
    #? man könnte die daten auch ganz an eine formatierungs funktione übergeben sowas wie title, channelId, thumbnail, channel Name läst sich auch so finden



        
def getChannelRecource(channelid):
    youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
    request = youtube.channels().list(
                part="snippet",
                id = channelid
            )
    try:
        response = request.execute() 
        
    except Exception as e:
        print(f"Error when trying to get Channel Recource error: {e}")
    channelRecource = []  
    channelRecource.append(response["items"][0]["id"])
    channelRecource.append(response["items"][0]["snippet"]["title"])
    channelRecource.append(response["items"][0]["snippet"]["thumbnails"]["default"]["url"])
    return channelRecource


def getVideoLength(videoid):
    youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
    request = youtube.videos().list(
                part="contentDetails",
                id = videoid
            )
    try:
        response = request.execute() 
    except Exception as e:
        print(f"video length error: {e}")
    videoLength = response["items"][0]["contentDetails"]["duration"]
    hourPatern = "[0-9]*H"
    minutePattern = "[0-9]*M"
    secondPattern = "[0-9]*S"
    videoLengthString = ""
    houres =  re.findall(hourPatern, videoLength)
    minutes = re.findall(minutePattern, videoLength)
    seconds = re.findall(secondPattern, videoLength)
    if houres:
        if len(minutes) == 0:
            minutes.append("00M")
        if len(seconds) == 0:
            seconds.append("00S")
        if len(minutes[0][:-1]) == 1:
            minutes[0] = "0" + minutes[0]
        if len(seconds[0][:-1]) == 1:
            seconds[0] = "0" + seconds[0]
        videoLengthString = houres[0][:-1] + ":" + minutes[0][:-1] + ":" + seconds[0][:-1]
    elif minutes:
        if len(seconds) == 0:
            seconds.append("00S")
        if len(seconds[0][:-1]) == 1:
            seconds[0] = "0" + seconds[0]
        videoLengthString  = minutes[0][:-1] + ":" + seconds[0][:-1]
    elif seconds:
        if len(seconds[0][:-1]) == 1:
            seconds[0] = "0" + seconds[0]
        videoLengthString = "0:" + seconds[0][:-1]
    else:
        raise Exception ("Video has no time that no bueno")

    return videoLengthString






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
    videoRecource[videoId] = {"videoLength":videoRecource[videoId],"videoTitle": videoTitle,"thumbnail":  vidoeThumbnail,"channelId": channelid,
                              "channelName": channelRecource[1],"channelBanner": channelRecource[2]}

    return videoRecource




def loadVidoeRecomendations():
    channelsarr = getSubscribedChannels(currentTopicChannelId)
    videosarr = getVideosofChannels(channelsarr)
    random.shuffle(videosarr)
    videoRecources = []
    for video in videosarr:
        videoRecource = getVideoRecourse(video)
        videoRecources.append(videoRecource)
    return videoRecources


