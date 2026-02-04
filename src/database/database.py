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
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Frontend', 'UCFbNIlppjAuEX4znoulh0Cw')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Backend', 'UC4SVo0Ue36XCfOyb5Lh1viQ UC8butISFwT-Wl7EV0hUK0BQ UC9HOZ53gnHP3f_b-wixS74g')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Bible', 'UCRKZqt7rf6_Lo5rFwuPTKmw UCTzZ2-byV7kigoeQ1ZQ39ig UCkY7QYZf3_ZnGQM6K_ju2aQ')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'ML/AI/LLM', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Engeeniring/Architekture', 'UCQnJlfHdJ2OolZSa4h2H5Rg UCaSCt8s_4nfkRglWCvNSDrg')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Motivation', 'UC5--wS0Ljbin1TjWQX6eafA UCsBjURrPoezykLs9EqgamOA')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'CyberSec', 'UC6biysICWOJ-C3P4Tyeggzg UC7e_BXvNfjKFCgqR4LkUe9A UC9c12UnfHIru-tZTbW-G3gQ UCJC0LxyEnw9yenVQxYanRzw')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'PersonalDevelopment', 'UCZe_ogqn3ZGC77M5gvk9dow ')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'AI SLOP', '')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Hardware', 'UCGKEMK3s-ZPbjVOIuAV8clQ')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Nachrichten', 'UC5NOEUbkLheQcaaRldYW5GA UCsBjURrPoezykLs9EqgamOA')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'Finanzen', 'UCFxPUPyzQQYaNfj0El4Ccqg UCeARcCUiZg79SQQ-2_XNlXQ UCkCGANrihzExmu9QiqZpPlQ UCkcnYVAVZQOB-nXHechtXDg')")
cursor.execute("INSERT INTO users VALUES ('Henning Agge', 'General', 'UC2Rxu8zyppEhjhZLlYL_iOQ UC8butISFwT-Wl7EV0hUK0BQ UCUyeluBRhGPCW4rPe_UvBZQ UCyFWoLmPTgZ3BkHIKMRSV1g')")