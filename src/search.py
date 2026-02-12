import googleapiclient.discovery
from variable import currentTopicChannelId
import os
from Ai.searchImprover import fixSpelling, improveQuery
Api_Key = os.environ.get('API_KEY')
api_service_name = "youtube"
api_version = "v3"


# man muss mall schauen das kommen ja videos und channel die müssen ja anders außsehen.
# eine funktion mit der man channel suchen kann aber auch videos 
# auch eine funktion die improvents zu deaktivieren das könnte man in den prompt ein bauen:
def searchYoutbe(query: str, type: str):
    speeledQuerry = fixSpelling(query)
    improvedQuery = improveQuery(speeledQuerry)
    print(f"Speeled query: {speeledQuerry}")
    print(f"Imporved query: {improvedQuery}")
    try:
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=Api_Key)
        request = youtube.search().list(
            part="snippet",
            channelId=currentTopicChannelId,
            maxResults=10,
            order="relevance",
            q=improvedQuery,
            type=type
        )
        response = request.execute()
    
    except Exception as e:
        print(f"There has been an error when requesting the Youtube Api for the Playlists of a Channel error: {e}")
        return []
    print(response.text)


