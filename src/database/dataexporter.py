import sqlite3
from dbconstants import dbName


def getChannelTopics(topic: str):
    connection = sqlite3.connect(dbName)
    cursor = connection.cursor()

    response = cursor.execute("SELECT * FROM users WHERE owner == 'Henning Agge' and topic == ?", (topic))
    return response