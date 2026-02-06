from database.datainteracter import createDbRecode
from Ai.databaseSorter import DbClasschooser
from recomendations import getLightChannelResource

def addNewChannelToDB(channelId):
    lightChannelResource = getLightChannelResource(channelid=channelId)
    bestFitPlaylist = DbClasschooser(channelName=lightChannelResource[0], channelDes=lightChannelResource[1])
    print(bestFitPlaylist)
    print(lightChannelResource)