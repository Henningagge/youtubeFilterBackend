import random
from constants import  Api_Key
import googleapiclient.discovery
import re
api_service_name = "youtube"
api_version = "v3"

def getSubscribedChannels(userChannelId):
    pass

def getVideosofChannels(channelsidarr):
    pass

def getChannelRecource(channelid):
    youtube = googleapiclient.discovery.build(api_service_name,api_version, developerKey=Api_Key)
    request = youtube.channels().list(
                part="snippet",
                id = channelid
            )
    try:
        response = request.execute() 
    except Exception as e:
        print(f"Channel Recource: {e}")
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
#! maybe solte ich das was das formating macht auslagern
def formatVideos(videoUrl, thumbnail, channelname, channelBanner, length):
    pass 
    #hier soll einfach ein json geabaut werden welches dann ans front entübergeben werden kann
    #? maybe auch nicht ich kann die ja so übergeben einfach schiecken muss mal schauen
def sendVideostoFrontend(formatedVideosarr):
    pass

def loadVidoeRecomendations(userChannelId):
    channelsarr = getSubscribedChannels(userChannelId)
    videosarr = getVideosofChannels(channelsarr)
    random.shuffle(videosarr)
    for channel in channelsarr:
        pass
    



#wie sieht ein video aus was dann ans front end geschicket werden soll
#
#
#   thumbnail=thumbnailurl
#   src="https://www.youtube.com/embed/{video_id}
#   channelName=Name
#   Channeldbanner=bannerurl
#   videoLenght= 1:23       #wie machen keine sekunden because i don't care ob video 0:30:35 oder 0:30:50
#