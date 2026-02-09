import sqlite3



def getChannelTopics(topic: str):
    #define connection and cursor
    connection = sqlite3.connect("users_subscribers.db")
    cursor = connection.cursor()

    response = cursor.execute(f"SELECT * FROM users WHERE owner == 'Henning Agge' and topic == {topic}")
    return response