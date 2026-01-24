from Playlists import getPlaylistViaChannelId, getVideosinPlaylist
import unittest
from topicSwap import switchTopic, resetToStadartTopic
import re
from recomendations import getChannelRecource, getVideoLength
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
        self.assertEqual(result, ['jFzwS7z2418', 'fc0V8GHYiOw'])

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
        expectedOutput = "{'PLg7eNtqimWhw6glG1BNZNmFAlLiGnXMGe': ['TimeTest', 'https://i.ytimg.com/vi/eB0zU5tnSPo/default.jpg'], 'PLg7eNtqimWhxzVBsWVm-rxpECNuUiEJ9w': ['hello mi matchu mitischo daloscho', 'https://i.ytimg.com/vi/hK0_mSvfEdo/default.jpg'], 'PLg7eNtqimWhyPUjoBZoWK-5VcIkQfuQ4x': ['Bible concepts', 'https://i.ytimg.com/vi/jFzwS7z2418/default.jpg']}"
        #process
        response = getPlaylistViaChannelId()
        print(f"kaölkfjsaölkjfölsakfjasl {response}")
        #check
        self.assertEqual(f"{response}", expectedOutput)

if __name__ == '__main__':
  unittest.main()