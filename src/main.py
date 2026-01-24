from constants import FilterHenning_Channelid, FilterHenning_User, Api_Key
from Playlists import getPlaylistViaChannelId, getVideosinPlaylist, openPlaylists
from recomendations import getSubscribedChannels, getVideosofChannels, loadVidoeRecomendations
from variable import currentTopicChannelId
def main():
    recomendations = loadVidoeRecomendations(currentTopicChannelId)



    #playlistids = getPlaylistViaChannelId()
  #  print(playlistids)
  #  for key in playlistids:
  #      result = getVideosinPlaylist(key)
 #       print("videoids in palylist")
 #       print(result)
 #       print(f"opening the Playlist: {key}")

 #       vidoeRecource = openPlaylists(key)
 #       print(vidoeRecource)

if __name__ == "__main__":
    main()






