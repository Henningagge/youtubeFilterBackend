from constants import FilterHenning_Channelid, FilterHenning_User, Api_Key
from Playlists import getPlaylistViaChannelId

def main():
    getPlaylistViaChannelId()

if __name__ == "__main__":
    main()
"""
Youtube Api Waht do i Need to do?

Playlists:
GET https://www.googleapis.com/youtube/v3/playlists

videos aus Playlists:




"""


#Diese anfrage gibt die alle Playlists ids die ein Channel hat
f"https://www.googleapis.com/youtube/v3/playlists?key={Api_Key}&part=contentDetails&channelId={FilterHenning_Channelid}&maxResults=10"
#dise anfrage gibt die die videos ids einer playlist du muss nurr die id bereit steleln
f"https://www.googleapis.com/youtube/v3/playlistItems?key={Api_Key}&part=contentDetails&playlistId=PLg7eNtqimWhyPUjoBZoWK-5VcIkQfuQ4x&maxResults=5"







#"id einer playlist"
"PLg7eNtqimWhxzVBsWVm-rxpECNuUiEJ9w"

#video id
"fc0V8GHYiOw"
#diese anfrage gibt die title und description von einem video mittels einer video id sowie das title bild in verschiedenen ausführungen
f"https://www.googleapis.com/youtube/v3/videos?key={Api_Key}&part=snippet&id=fc0V8GHYiOw"


#note es gibt eine funktion bei videos/list : list (my liked videos)
#nutze iframe
'src="https://www.youtube.com/embed/{video_id}"'


#Channels via channel id:
f"https://youtube.googleapis.com/youtube/v3/subscriptions?part=snippet%2CcontentDetails&channelId=UCsd4OmYbE6BeYEdm-Vn7pcQ&key={Api_Key}&maxResults=10"

#Videos of channels:

f"https://www.googleapis.com/youtube/v3/search?key={Api_Key}&channelId=UCTzZ2-byV7kigoeQ1ZQ39ig&part=snippet,id&order=date&maxResults=20"

#findet channel by name:
f"https://www.googleapis.com/youtube/v3/search?key={Api_Key}&part=snippet&q=Ear to Hear&type=channel"



