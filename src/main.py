from recomendations import getChannelRecource, getSubscribedChannels, getLightChannelResource
from variable import currentTopicChannelId


def main():
    recomendations = getSubscribedChannels(currentTopicChannelId)
    print(recomendations)
    # result = getPlaylistViaChannelId()
    channel = getChannelRecource("UCFbNIlppjAuEX4znoulh0Cw")
    print(channel)
    light = getLightChannelResource("UCFbNIlppjAuEX4znoulh0Cw")
    print(light)
    pass

    # result2 = openPlaylist("PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf")


if __name__ == "__main__":
    main()
