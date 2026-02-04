from recomendations import getChannelRecource, getSubscribedChannels
from variable import currentTopicChannelId


def main():
    recomendations = getSubscribedChannels(currentTopicChannelId)
    print(recomendations)
    # result = getPlaylistViaChannelId()
    pass

    # result2 = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")


if __name__ == "__main__":
    main()
