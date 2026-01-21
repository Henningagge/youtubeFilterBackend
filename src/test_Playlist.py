from Playlists import getPlaylistViaChannelId

import unittest



class TestGetPlaylist(unittest.TestCase):
    def testNormalPattern(self):
        expectedOutput = "['PLg7eNtqimWhxzVBsWVm-rxpECNuUiEJ9w', 'PLg7eNtqimWhyPUjoBZoWK-5VcIkQfuQ4x']"
        response = getPlaylistViaChannelId()
        self.assertEqual(f"{response}", expectedOutput)

if __name__ == '__main__':
  unittest.main()