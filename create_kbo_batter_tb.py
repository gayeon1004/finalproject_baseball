import sqlite3

# print(sqlite3.version) 

con = sqlite3.connect('dbdb.db')
# print(type(con))
cursor = con.cursor() 

sql = "DROP TABLE IF EXISTS 'kbo_batter'"
cursor.execute(sql)
con.commit()

sql = '''
CREATE TABLE "kbo_batter" (
    "rank"    INTEGER NOT NULL,
    "team"  TEXT NOT NULL,
    "name"  TEXT NOT NULL,
    "hra"  REAL NOT NULL,
    "hr"  INTEGER NOT NULL,
    "rbi"  INTEGER NOT NULL,
    "sb"  INTEGER NOT NULL,
    "ops" REAL NOT NULL,
    "war"  REAL NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql)
con.commit() 
con.close()