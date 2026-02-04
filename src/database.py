import sqlite3

#define connection and cursor
connection = sqlite3.connect("users_subscribers.db")
cursor = connection.cursor()

# create tables
command = """CREATE TABLE IF NOT EXISTS users(owner TEXT PRIMARY KEY, topicchannel TEXT, subscribers TEXT)"""
cursor.execute(command)

#?macht owner nicht nur sin wen ich eine login habe oder den owner wechseln kann
#add data
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'LikedVideos', 'liked')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Frontend', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Backend', 'UC4SVo0Ue36XCfOyb5Lh1viQ ')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Bible', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'ML/AI/LLM', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Engeeniring/Architekture', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Motivation', 'UC5--wS0Ljbin1TjWQX6eafA ')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'CyberSec', 'UC6biysICWOJ-C3P4Tyeggzg ')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'PersonalDevelopment', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'AI SLOP', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Hardware', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Nachrichten', 'UC5NOEUbkLheQcaaRldYW5GA')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Finanzen', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'General', 'UC2Rxu8zyppEhjhZLlYL_iOQ ')")