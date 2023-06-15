import sqlite3

# print(sqlite3.version) 

con = sqlite3.connect('dbdb.db')
# print(type(con))
cursor = con.cursor() 

sql = "DROP TABLE IF EXISTS 'kbo_picher'"
cursor.execute(sql)
con.commit()

sql = '''
CREATE TABLE "kbo_picher" (
    "rank"    INTEGER NOT NULL,
    "team"  TEXT NOT NULL,
    "name"  TEXT NOT NULL,
    "era"  REAL NOT NULL,
    "w"  INTEGER NOT NULL,
    "sv"  INTEGER NOT NULL,
    "kk"  INTEGER NOT NULL,
    "whip" REAL NOT NULL,
    "war"  REAL NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql)
con.commit() 
con.close()