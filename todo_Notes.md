3. code auf räumen
4. front end fertig machen
5. Tests für alles schreiben
6. Auch mock tests schreiben
7. Build Cd
8. edcase wie wen playlist lehr ist oder keine abonierten channels
9. erklärung und cloning in die readme schreiben
10. für oauth2 umbauen damit ich private stellen kann
11. so ein banner von boot.dev und das banner mit wie viel prozent der test passen
12. meinen funktion gut exceptions geben wen sie das brauchen
13. flake8 pyright und die anderen sachen die die im Team benutzen einbauen
14. likes geben
15. liked sowie später ansehen playylists krigen

# Fragen

brauche ich eine easy version zum registrieren von nutzer weil das soll ja bei github auch jemand bauen können
Brauchen ich eine DB für das chaching von daten und dann nur einmal täglich massiven aufwand machen?

will ich eine Suchfunktion?

will ich Ai nutzen um die Search zu Optimieren? (warscheinlich nicht aber yagni is usless)

Ist Werbung ein Probelm muss ich addblocker bauen?

Will ich privates spähre dann muss ich alles mit oauth2 nachbauen
Notes:

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

test test
