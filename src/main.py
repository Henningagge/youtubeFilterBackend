from constants import FilterHenning_Channelid, FilterHenning_User, Api_Key
from Playlists import getPlaylistViaChannelId, getVideosinPlaylist, openPlaylist
from recomendations import getSubscribedChannels, getVideosofChannels, loadVidoeRecomendations
from variable import currentTopicChannelId
def main():
    recomendations = loadVidoeRecomendations(currentTopicChannelId)
    result = getPlaylistViaChannelId()
    print(recomendations)
    print(result)
    result2 = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")
    print(result2)



if __name__ == "__main__":
    main()






