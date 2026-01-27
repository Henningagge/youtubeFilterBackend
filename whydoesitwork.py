
#* CHATGPT: FUNKTIONIERT
import unittest
from unittest.mock import patch, Mock, MagicMock

class TestGetChannelResource(unittest.TestCase):
    @patch("googleapiclient.discovery.build")
    def testGetChannelResource(self, mock_build):
        # Mock-Objekte erstellen
        mock_youtube = MagicMock()
        mock_channels = Mock()
        mock_channels_list = Mock()  # Mock für das, was list() zurückgibt
        mock_execute = Mock()

        # Konfigurieren der Rückgabewerte (wichtig!)
        response_dict = {'kind': 'youtube#channelListResponse', 'etag': '6NHK8hBiM6aq9XgEK4v4EvSuhYI', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': '9_aCofqtgu2M7QEKlTUsHdQ0YCM', 'id': 'UCsd4OmYbE6BeYEdm-Vn7pcQ', 'snippet': {'title': 'Henning Filter', 'description': '', 'customUrl': '@henningfilter', 'publishedAt': '2026-01-20T18:03:42.546747Z', 'thumbnails': {'default': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s88-c-k-c0x00ffffff-no-rj', 'width': 88, 'height': 88}, 'medium': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s240-c-k-c0x00ffffff-no-rj', 'width': 240, 'height': 240}, 'high': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s800-c-k-c0x00ffffff-no-rj', 'width': 800, 'height': 800}}, 'localized': {'title': 'Henning Filter', 'description': ''}}}]}

        mock_execute.return_value = response_dict
        mock_channels_list.execute.return_value = response_dict

        # WICHTIG: Hier wird festgelegt, was .list() zurückgibt
        mock_channels.list.return_value = mock_channels_list

        # Hier definieren wir, was mock_youtube.channels() zurückgeben soll
        mock_youtube.channels.return_value = mock_channels  # Korrekter Mock für channels()
        mock_build.return_value = mock_youtube

        # Ausführen der Funktion mit den gemockten Objekten
        currentTopicChannelId = "UCsd4OmYbE6BeYEdm-Vn7pcQ"
        Api_Key = "test_api_key" #Du brauchst einen Wert für Api_Key
        from your_module import getChannelRecource  # Ersetze your_module
        user_data = getChannelRecource(currentTopicChannelId, Api_Key)

        # Assertions
        mock_build.assert_called_with("youtube", "v3", developerKey=Api_Key)
        mock_youtube.channels.assert_called_once()  # Überprüfe, ob channels() aufgerufen wurde
        mock_channels.list.assert_called_once_with(part="snippet", id=currentTopicChannelId)  # Hier wird der Aufruf von list() geprüft
        mock_channels_list.execute.assert_called_once()  # Hier wird der Aufruf von execute geprüft

        expected_data = ['UCsd4OmYbE6BeYEdm-Vn7pcQ', 'Henning Filter', 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s88-c-k-c0x00ffffff-no-rj']
        self.assertEqual(user_data, expected_data)

#* CHATGPT FUNTIONIERT NICHT ERORR EXPECTED LIST TO BE CALLED 
class TestGetChannelResource(unittest.TestCase):
    @patch("googleapiclient.discovery.build")
    def testGetChannelResource(self, mock_build):
        mock_youtube = MagicMock()
        mock_channels = Mock()
        mock_channels_list = Mock()
        mock_execute = Mock()

        
        response_dict = {'kind': 'youtube#channelListResponse', 'etag': '6NHK8hBiM6aq9XgEK4v4EvSuhYI', 'pageInfo': {'totalResults': 1, 'resultsPerPage': 5}, 'items': [{'kind': 'youtube#channel', 'etag': '9_aCofqtgu2M7QEKlTUsHdQ0YCM', 'id': 'UCsd4OmYbE6BeYEdm-Vn7pcQ', 'snippet': {'title': 'Henning Filter', 'description': '', 'customUrl': '@henningfilter', 'publishedAt': '2026-01-20T18:03:42.546747Z', 'thumbnails': {'default': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s88-c-k-c0x00ffffff-no-rj', 'width': 88, 'height': 88}, 'medium': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s240-c-k-c0x00ffffff-no-rj', 'width': 240, 'height': 240}, 'high': {'url': 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s800-c-k-c0x00ffffff-no-rj', 'width': 800, 'height': 800}}, 'localized': {'title': 'Henning Filter', 'description': ''}}}]}

        mock_execute.return_value = response_dict
        mock_channels_list.execute.return_value = response_dict
        mock_channels_list.list.return_value = mock_channels_list
        mock_channels.list.return_value = mock_channels_list

        
        mock_youtube.channels.return_value = mock_channels 
        mock_build.return_value = mock_youtube

        user_data = getChannelRecource(currentTopicChannelId)

        
        mock_build.assert_called_with("youtube", "v3", developerKey=Api_Key)
        mock_youtube.channels.assert_called_once()
        mock_channels_list.list.assert_called_once_with(part="snippet", id=currentTopicChannelId)
        mock_channels_list.execute.assert_called_once() 

        expected_data = ['UCsd4OmYbE6BeYEdm-Vn7pcQ', 'Henning Filter', 'https://yt3.ggpht.com/ytc/AIdro_n17eVS6yOwSEgbNTgXc4n9JeOKRE9MMEESD8Bfcg_tgLUU3ZPzBmNs64A-tbv0zyDUoA=s88-c-k-c0x00ffffff-no-rj']
        self.assertEqual(user_data, expected_data)



#*MY CODE: NOT WORKING ERROR: CHANNEL EXPECTED TO BE CALLED BUT IS 0 TIMES CALLES
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

