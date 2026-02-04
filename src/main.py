from constants import FilterHenning_Channelid, FilterHenning_User
from playlists import getPlaylistViaChannelId, getVideosinPlaylist, openPlaylist
from recomendations import getSubscribedChannels, getVideosofChannels, loadVidoeRecomendations, getChannelRecource
from variable import currentTopicChannelId


def main():
    recomendations = getChannelRecource(currentTopicChannelId)
    print(recomendations)
    # result = getPlaylistViaChannelId()
    pass

    # result2 = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")


if __name__ == "__main__":
    main()
