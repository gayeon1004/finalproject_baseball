import sqlite3

# print(sqlite3.version) 

con = sqlite3.connect('dbdb.db')
# print(type(con))
cursor = con.cursor() 

sql = "DROP TABLE IF EXISTS 'mlb_american_pitcher'"
cursor.execute(sql)
con.commit()

sql = '''
CREATE TABLE "mlb_american_pitcher" (
    "rank"    INTEGER NOT NULL,
    "teamName"  TEXT NOT NULL,
    "playerName"  TEXT NOT NULL,
    "ERA"  REAL NOT NULL,
    "W"  INTEGER NOT NULL,
    "SV"  INTEGER NOT NULL,
    "SO"  INTEGER NOT NULL,
    "H" REAL NOT NULL,
    "BB"  REAL NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql)
con.commit() 
con.close()