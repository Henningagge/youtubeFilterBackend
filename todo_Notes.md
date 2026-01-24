1. Die daten schöner machen damit vor den werten steht was das ist z.b videoTitle: "How the wised man was unhappy"
2. die video sachen fertig machen
3. das generele html desing machen
4. tailwind einbinden
5. interaktivity für das html.
6. die todos machen
7. code auf räumen
8. front end fertig machen
9. Tests für alles schreiben
10. Auch mock tests schreiben
11. die VideoLengt formatieren
12. Create Ci
13. Build Cd
    14edcase wie wen playlist lehr ist oder keine abonierten channels

# Fragen

Brauchen ich eine DB für das chaching von daten und dann nur einmal täglich massiven aufwand machen?

wie mock man eigentlich

will ich eine Such funktion
will ich Ai nutzen um die Search zu Optimieren? (warscheinlich nicht aber yagni is usless)

Ist Werbung ein Probelm muss ich addblocker bauen?

Notes:

#! https://www.youtube.com/watch?v={videoId} um sich was anzuschauen
#! <iframe width="560" height="315" src="https://www.youtube.com/embed/{vidoeId}"
#! frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

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
