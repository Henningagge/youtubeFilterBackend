import sqlite3
from dbconstants import dbName

def initDatabase():

    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    command = """CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    owner VARCHAR(255) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    subscribers VARCHAR(255));"""
    cursor.execute(command)


    cursor.execute("INSERT INTO users VALUES (1,'Henning Agge', 'LikedVideos', 'liked')")
    cursor.execute("INSERT INTO users VALUES (2,'Henning Agge', 'Frontend', 'UCFbNIlppjAuEX4znoulh0Cw')")
    cursor.execute("INSERT INTO users VALUES (3,'Henning Agge', 'Backend', 'UC4SVo0Ue36XCfOyb5Lh1viQ UC8butISFwT-Wl7EV0hUK0BQ UC9HOZ53gnHP3f_b-wixS74g')")
    cursor.execute("INSERT INTO users VALUES (4,'Henning Agge', 'test', 'UCRKZqt7rf6_Lo5rFwuPTKmw UCTzZ2-byV7kigoeQ1ZQ39ig UCkY7QYZf3_ZnGQM6K_ju2aQ')")
    cursor.execute("INSERT INTO users VALUES (5,'Henning Agge', 'ML/AI/LLM', '')")
    cursor.execute("INSERT INTO users VALUES (6,'Henning Agge', 'Engeeniring/Architekture', 'UCQnJlfHdJ2OolZSa4h2H5Rg UCaSCt8s_4nfkRglWCvNSDrg')")
    cursor.execute("INSERT INTO users VALUES (7,'Henning Agge', 'Motivation', 'UC5--wS0Ljbin1TjWQX6eafA UCsBjURrPoezykLs9EqgamOA')")
    cursor.execute("INSERT INTO users VALUES (8,'Henning Agge', 'CyberSec', 'UC6biysICWOJ-C3P4Tyeggzg UC7e_BXvNfjKFCgqR4LkUe9A UC9c12UnfHIru-tZTbW-G3gQ UCJC0LxyEnw9yenVQxYanRzw')")
    cursor.execute("INSERT INTO users VALUES (9,'Henning Agge', 'PersonalDevelopment', 'UCZe_ogqn3ZGC77M5gvk9dow ')")
    cursor.execute("INSERT INTO users VALUES (10,'Henning Agge', 'AI SLOP', '')")
    cursor.execute("INSERT INTO users VALUES (11,'Henning Agge', 'Hardware', 'UCGKEMK3s-ZPbjVOIuAV8clQ')")
    cursor.execute("INSERT INTO users VALUES (12,'Henning Agge', 'News/Nachrichten', 'UC5NOEUbkLheQcaaRldYW5GA UCsBjURrPoezykLs9EqgamOA')")
    cursor.execute("INSERT INTO users VALUES (13,'Henning Agge', 'Finace/Finanzen', 'UCFxPUPyzQQYaNfj0El4Ccqg UCeARcCUiZg79SQQ-2_XNlXQ UCkCGANrihzExmu9QiqZpPlQ UCkcnYVAVZQOB-nXHechtXDg')")
    cursor.execute("INSERT INTO users VALUES (14,'Henning Agge', 'General', 'UC2Rxu8zyppEhjhZLlYL_iOQ UC8butISFwT-Wl7EV0hUK0BQ UCUyeluBRhGPCW4rPe_UvBZQ UCyFWoLmPTgZ3BkHIKMRSV1g')")
    connection.commit()
    connection.close()


def addChannelToTopic(playlist1: str, playlist2: str, channelId: str):
    
    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()
    
    if playlist1 != "----":
        currentChannel1 = cursor.execute("SELECT subscribers FROM users where topic is ?", (playlist1))
        cursor.execute("UPDATE users SET subscribers = ? WHERE topic = ?", (currentChannel1 + " " + channelId, playlist1))
        connection.commit()

    if playlist2 != "----":
        currentChannel2 = cursor.execute("SELECT subscribers FROM users where topic is ?", (playlist2))
        cursor.execute("UPDATE users SET subscribers = ? WHERE topic = ?", (currentChannel2 + " " + channelId, playlist2))
        connection.commit()
    connection.close()


def checkChannelInDb(chnnelId: str):
    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()
    
    response = cursor.execute("SELECT * FROM users")
    for row in response:
        splitChannelIds = row[3].split(" ")
        if chnnelId in splitChannelIds:
            connection.close()
            return True
    connection.close()

checkChannelInDb("UC2Rxu8zyppEhjhZLlYL_iOQ")

def getChannelsForTopic(topic: str):
    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE topic = ?", (topic,))
    results = cursor.fetchall()
    connection.close()
    return results[0][3]
print(getChannelsForTopic("Hardware"))