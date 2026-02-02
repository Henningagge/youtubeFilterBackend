from playlists import getPlaylistViaChannelId, getVideosinPlaylist
import unittest
from topicSwap import switchTopic, resetToStadartTopic
import re 
from unittest.mock import patch, Mock, MagicMock
import requests
import googleapiclient.discovery
from recomendations import getChannelRecource, getVideoLength, loadVidoeRecomendations
from variable import currentTopicChannelId
import os
Api_Key = os.environ.get('API_KEY')
class TestSwitchTopi(unittest.TestCase):
    def testNormalPatternSwitch(self):
        input = "hallo123"
        output = 'currentTopicChannelId = "hallo123"'
        switchTopic(input)
        with open("./src/variable.py", "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.fullmatch(output, line):
                    self.assertEqual(output, line)
                    resetToStadartTopic()
    def testNoPattern(self):
        input = ""
        output = 'currentTopicChannelId = ""'
        switchTopic(input)
        with open("./src/variable.py", "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.fullmatch(output, line):
                    self.assertEqual(output, line)
                    resetToStadartTopic()

class TestRestTopic(unittest.TestCase):
    def testNormalReset(self):
        output = 'currentTopicChannelId = "UCsd4OmYbE6BeYEdm-Vn7pcQ"'
        resetToStadartTopic()
        with open("./src/variable.py", "r") as file:
            lines = file.readlines()
            for line in lines:
                if re.fullmatch(output, line):
                    self.assertEqual(output, line)

class TestVideosinPlaylist(unittest.TestCase):
    def testNormalResult(self):
        #given
        input = "PLg7eNtqimWhyPUjoBZoWK-5VcIkQfuQ4x"
        #process
        result = getVideosinPlaylist(input)
        #check
        self.assertEqual(result, [])

class TestVideoLengthFuntion(unittest.TestCase):
    def testHouresInput(self):
        #given
        input = "QK79xplUqlU"
        #process
        viedeoLength = getVideoLength(input)
        #check
        self.assertEqual(viedeoLength, '2:07:47' )

    def testMinutesInput(self):
        #given
        input = "jFzwS7z2418"
        #process
        viedeoLength = getVideoLength(input)
        #check
        self.assertEqual(viedeoLength, '27:27' )

    def testMinutesInput2(self):
        #given
        input = "0kfpO8Up7Ek"
        #process
        viedeoLength = getVideoLength(input)
        #check
        self.assertEqual(viedeoLength, '50:49' )
    def testSecondsInput(self):
        #given
        input = "eB0zU5tnSPo"
        #process
        viedeoLength = getVideoLength(input)
        #check
        self.assertEqual(viedeoLength, '0:21' )
    def testPrecedingZerosMinutes(self):
        #given
        input = "SxuYDyk7iTw"
        #process
        viedeoLength = getVideoLength(input)
        #check
        self.assertEqual(viedeoLength, '1:00:01' )
    def testPrecedingZerosseconds(self):
        #given
        input = "GGlGYyiJfzI"
        #process
        viedeoLength = getVideoLength(input)
        #check
        self.assertEqual(viedeoLength, '13:09' )


class TestGetPlaylist(unittest.TestCase):
    def testNormalPattern(self):
        #given
        expectedOutput = "{'PLg7eNtqimWhyn2z4WaBdbrDTupcZo_O3U': {'PlaylistTitle': 'ksajfsalkjfsak', 'PlaylistThumbnail': 'https://i.ytimg.com/vi/iaAHQPM1AOk/default.jpg'}, 'PLg7eNtqimWhzsgyYtVznG0eijxiWtzFEG': {'PlaylistTitle': 'dfksajfksaj', 'PlaylistThumbnail': 'https://i.ytimg.com/vi/IQbWbxfomQ4/default.jpg'}, 'PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf': {'PlaylistTitle': 'Garrot', 'PlaylistThumbnail': 'https://i.ytimg.com/vi/tTDhJq7amlU/default.jpg'}}"
        #process
        response = getPlaylistViaChannelId()
        #check
        self.assertEqual(f"{response}", expectedOutput)

class TestGetChannelRecource(unittest.TestCase):
    def testNormalChannelId(self):
        #given
        input = "UCTzZ2-byV7kigoeQ1ZQ39ig"
        #process
        result = getChannelRecource(input)
        #check
        self.assertEqual(result, ["UCTzZ2-byV7kigoeQ1ZQ39ig", 'Ear to Hear', 'https://yt3.ggpht.com/oe2rtGqTvV-JKIBnUWbvbzVvoDP4_Uy3S8ZqMuUuIYJCdOOVNmlrVOviOlI8kX0CUCyV2v-Yvg=s88-c-k-c0x00ffffff-no-rj'])


class TestMockGetPlaylists(unittest.TestCase):

    @patch("googleapiclient.discovery.build")
    def testNormalData(self, mock_build):
        mock_youtube = Mock()
        mock_playlists = Mock()
        mock_playlists_list = Mock()
        mock_execute = Mock()

        response_dict = {'kind': 'youtube#playlistListResponse', 'etag': '7GtmixPZkRuZ4i83gsgHJQePSTU', 'nextPageToken': 'CAUQAA', 'pageInfo': {'totalResults': 6, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#playlist', 'etag': 'ODuDxSWB8jFStY7WfWGxysKday8', 'id': 'PLg7eNtqimWhyn2z4WaBdbrDTupcZo_O3U', 'snippet': {'publishedAt': '2026-01-26T06:33:43.91067Z', 'channelId': 'UCsd4OmYbE6BeYEdm-Vn7pcQ', 'title': 'ksajfsalkjfsak', 'description': '', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/iaAHQPM1AOk/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/iaAHQPM1AOk/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/iaAHQPM1AOk/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/iaAHQPM1AOk/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/iaAHQPM1AOk/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': 'Henning Filter', 'localized': {'title': 'ksajfsalkjfsak', 'description': ''}}}, {'kind': 'youtube#playlist', 'etag': 'ckoSlizL-PGfpRi0ajCLCb4oe4U', 'id': 'PLg7eNtqimWhzsgyYtVznG0eijxiWtzFEG', 'snippet': {'publishedAt': '2026-01-26T06:33:24.623843Z', 'channelId': 'UCsd4OmYbE6BeYEdm-Vn7pcQ', 'title': 'dfksajfksaj', 'description': '', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/IQbWbxfomQ4/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/IQbWbxfomQ4/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/IQbWbxfomQ4/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/IQbWbxfomQ4/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/IQbWbxfomQ4/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': 'Henning Filter', 'localized': {'title': 'dfksajfksaj', 'description': ''}}}, {'kind': 'youtube#playlist', 'etag': 'yjHceQt0bqW8Ni64RmwuZyUqGsM', 'id': 'PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf', 'snippet': {'publishedAt': '2026-01-26T06:33:07.659169Z', 'channelId': 'UCsd4OmYbE6BeYEdm-Vn7pcQ', 'title': 'Garrot', 'description': '', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/tTDhJq7amlU/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/tTDhJq7amlU/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/tTDhJq7amlU/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/tTDhJq7amlU/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/tTDhJq7amlU/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': 'Henning Filter', 'localized': {'title': 'Garrot', 'description': ''}}}]}

        mock_execute.return_value = response_dict
        mock_playlists_list.execute.return_value = response_dict
        mock_playlists.list.return_value = mock_playlists_list
        mock_youtube.playlists.return_value = mock_playlists
        mock_build.return_value = mock_youtube

        user_data = getPlaylistViaChannelId()

        mock_build.assert_called_with("youtube", "v3", developerKey=Api_Key)
        mock_youtube.playlists.assert_called_once()
        mock_playlists.list.assert_called_once_with(part="snippet", channelId=currentTopicChannelId)

        expected_data = {
            'PLg7eNtqimWhyn2z4WaBdbrDTupcZo_O3U': {
                'PlaylistTitle': 'ksajfsalkjfsak',
                'PlaylistThumbnail': 'https://i.ytimg.com/vi/iaAHQPM1AOk/default.jpg'
            },
            'PLg7eNtqimWhzsgyYtVznG0eijxiWtzFEG': {
                'PlaylistTitle': 'dfksajfksaj',
                'PlaylistThumbnail': 'https://i.ytimg.com/vi/IQbWbxfomQ4/default.jpg'
            },
            'PLg7eNtqimWhwQsTr__Npprv7O26GBC8Yf': {
                'PlaylistTitle': 'Garrot',
                'PlaylistThumbnail': 'https://i.ytimg.com/vi/tTDhJq7amlU/default.jpg'
            }
        }
        self.assertEqual(user_data, expected_data)


    @patch("googleapiclient.discovery.build")
    def testGetPlaylistEmpty(self, mock_build):
        mock_youtube = Mock()
        mock_playlists = Mock()
        mock_playlists_list = Mock()
        mock_execute = Mock()

        response_dict = {'kind': 'youtube#playlistListResponse', 'etag': '7GtmixPZkRuZ4i83gsgHJQePSTU','nextPageToken': 'CAUQAA', 'pageInfo': {'totalResults': 6, 'resultsPerPage': 5}, 'items': []}
        
        mock_execute.return_value = response_dict
        mock_playlists_list.execute.return_value = response_dict
        mock_playlists.list.return_value = mock_playlists_list
        mock_youtube.playlists.return_value = mock_playlists
        mock_build.return_value = mock_youtube

        user_data = getPlaylistViaChannelId()

        mock_build.assert_called_with("youtube", "v3", developerKey=Api_Key)
        mock_youtube.playlists.assert_called_once()
        mock_playlists.list.assert_called_once_with(part="snippet", channelId=currentTopicChannelId)

        expected_data = {}

        self.assertEqual(user_data, expected_data)


#! auch noch tests für fehlerund andere id also keine id und falsche id
"""
class TestGetChannelResource(unittest.TestCase):
    @patch("googleapiclient.discovery.build")
    def testGetChannelResource(self, mock_build):
        mock_youtube = MagicMock()
        mock_channels = Mock()
        mock_execute = Mock()


        response_dict = {'kind': 'youtube#channelListResponse', 'etag': '6NHK8hBiM6aq9XgEK4v4EvSuhYI', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': '9_aCofqtgu2M7QEKlTUsHdQ0YCM', 'id': 'UCsd4OmYbE6BeYEdm-Vn7pcQ', 'snippet': {'title': 'Henning Filter', 'description': '', 'customUrl': '@henningfilter', 'publishedAt': '2026-01-20T18:03:42.546747Z', 'thumbnails': {'default': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s88-c-k-c0x00ffffff-no-rj', 'width': 88, 'height': 88}, 'medium': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s240-c-k-c0x00ffffff-no-rj', 'width': 240, 'height': 240}, 'high': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s800-c-k-c0x00ffffff-no-rj', 'width': 800, 'height': 800}}, 'localized': {'title': 'Henning Filter', 'description': ''}}}]}

        mock_execute.return_value = response_dict
        mock_channels.execute.return_value = response_dict
        mock_channels.list.return_value = mock_channels
        mock_build.return_value = mock_youtube

        user_data = getChannelRecource(currentTopicChannelId)

        mock_build.assert_called_with("youtube", "v3", developerKey= Api_Key)
        mock_youtube.channel.assert_called_once()
        mock_channels.list.assert_called_once_with(part="snippet", id=currentTopicChannelId)

        expected_data = ['UCsd4OmYbE6BeYEdm-Vn7pcQ', 'Henning Filter', 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s88-c-k-c0x00ffffff-no-rj']
        
        self.assertEqual(user_data, expected_data)
"""


#todo hier ist etwas sus ich weiß garnicht wieso ich youtube moke die funktion ruft nur funktionen auf
#todo bessere möglichkeit finden das zu testen vileicht subfunktions mocken
#* merk dir das shuffeld und du kannst xor machen wen du zwei responses hast
"""
class TestRecomendations(unittest.TestCase):
    @patch("googleapiclient.discovery.build")
    def testRecomendationResponse(self, mock_build):
        mock_youtube = Mock()
        mock_videos = Mock()
        mock_execute = Mock()

        response_dict = {'HFNgi-NYd18': {'videoLength': '22:34', 'videoTitle': '😂🤯Wir MACHEN ihn zum HUND! - ASOZIALSTE FOLGE ARC RAIDERS EVER mit ZARBEX und MARLI | Trymacs', 'thumbnail': 'https://i.ytimg.com/vi/HFNgi-NYd18/default.jpg', 'channelId': 'UC6Gc4KQ1ueDnh8x7plaAD3w', 'channelName': 'Trymacs', 'channelBanner': 'https://yt3.ggpht.com/ytc/AIdro_nmKhHDyPVOMAkIZ2uUVYJrKKnTvPlMhQTSvX-kSlD787A=s88-c-k-c0x00ffffff-no-rj'}}, {'j4K99IZTStQ': {'videoLength': '1:04:47', 'videoTitle': '24 STUNDEN MINECRAFT AM STÜCK SPIELEN (WELT = 100% WASSER)', 'thumbnail': 'https://i.ytimg.com/vi/j4K99IZTStQ/default.jpg', 'channelId': 'UCgZpwegd4AdDlZNrIamIgRw', 'channelName': 'BastiGHG', 'channelBanner': 'https://yt3.ggpht.com/s92_ZA6Dc-TmMI1zSZFtGcXv4Rrsl3XeP8hE2HUc402u18pfsriNkWrkLtqXAfjIq1K9Zi5D2p8=s88-c-k-c0x00ffffff-no-rj'}}

        mock_execute.return_value = response_dict
        mock_videos.excute.return_value = response_dict
        mock_youtube.playlists.return_value = mock_videos
        mock_build.return_value = mock_youtube

        user_data = loadVidoeRecomendations()

        mock_build.assert_called_with("youtube", "v3", developerKey = Api_Key)
        mock_youtube.videos.assert_called_once()
        mock_videos.list.assert_called_once_with(part="snippet", channelId=currentTopicChannelId)

        expected_data = [{'HFNgi-NYd18': {'videoLength': '22:34', 'videoTitle': '😂🤯Wir MACHEN ihn zum HUND! - ASOZIALSTE FOLGE ARC RAIDERS EVER mit ZARBEX und MARLI | Trymacs', 'thumbnail': 'https://i.ytimg.com/vi/HFNgi-NYd18/default.jpg', 'channelId': 'UC6Gc4KQ1ueDnh8x7plaAD3w', 'channelName': 'Trymacs', 'channelBanner': 'https://yt3.ggpht.com/ytc/AIdro_nmKhHDyPVOMAkIZ2uUVYJrKKnTvPlMhQTSvX-kSlD787A=s88-c-k-c0x00ffffff-no-rj'}}, {'j4K99IZTStQ': {'videoLength': '1:04:47', 'videoTitle': '24 STUNDEN MINECRAFT AM STÜCK SPIELEN (WELT = 100% WASSER)', 'thumbnail': 'https://i.ytimg.com/vi/j4K99IZTStQ/default.jpg', 'channelId': 'UCgZpwegd4AdDlZNrIamIgRw', 'channelName': 'BastiGHG', 'channelBanner': 'https://yt3.ggpht.com/s92_ZA6Dc-TmMI1zSZFtGcXv4Rrsl3XeP8hE2HUc402u18pfsriNkWrkLtqXAfjIq1K9Zi5D2p8=s88-c-k-c0x00ffffff-no-rj'}}]

        self.assertEqual(user_data, expected_data)
"""
if __name__ == '__main__':
  unittest.main()