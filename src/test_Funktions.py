from Playlists import getPlaylistViaChannelId, getVideosinPlaylist
import unittest
from topicSwap import switchTopic, resetToStadartTopic
import re

class TestSwitchTopi(unittest.TestCase):
    def testNormalPattern(self):
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
        #result
        result = getVideosinPlaylist(input)
        #check
        self.assertEqual(result, ['jFzwS7z2418', 'fc0V8GHYiOw'])



class TestGetPlaylist(unittest.TestCase):
    def testNormalPattern(self):
        expectedOutput = "['PLg7eNtqimWhxzVBsWVm-rxpECNuUiEJ9w', 'PLg7eNtqimWhyPUjoBZoWK-5VcIkQfuQ4x']"
        response = getPlaylistViaChannelId()
        self.assertEqual(f"{response}", expectedOutput)

if __name__ == '__main__':
  unittest.main()