from variable import currentTopicChannelId
import re
from recomendations import loadVidoeRecomendations
def switchTopic(userChannelId):
    pattern = 'currentTopicChannelId = "[a-z, A-Z,0-9,$&+,:;=?@#|<>.^*()%!-]*"'

    variableFile = "./src/variable.py"
    try:
        with open(variableFile, "r") as file:
            lines = file.readlines()
        with open(variableFile, "w") as file:
            for line in lines:
                if re.fullmatch(pattern, line):
                    file.write(f'currentTopicChannelId = \"{userChannelId}\"')
                else:
                    file.write(line)
    except FileNotFoundError as e:
        print(f"The file a path: {variableFile} could not be found error: {e}")
    except Exception as e:
        print(f"There has been an error when replacing the topic id error: {e}")
    #loadVidoeRecomendations(userChannelId) #mayber muss man hier auch noch was returnenn oder in ein file schreiben
    return


def resetToStadartTopic():
    standarttopicId = "UCsd4OmYbE6BeYEdm-Vn7pcQ"
    switchTopic(standarttopicId)
    #loadVidoeRecomendations(standarttopicId)