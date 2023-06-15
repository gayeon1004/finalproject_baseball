import sqlite3

# print(sqlite3.version) 

con = sqlite3.connect('dbdb.db')
# print(type(con))
cursor = con.cursor() 

sql = "DROP TABLE IF EXISTS 'mlb_national_batter'"
cursor.execute(sql)
con.commit()

sql = '''
CREATE TABLE "mlb_national_batter" (
    "rank"    INTEGER NOT NULL,
    "teamName"  TEXT NOT NULL,
    "playerName"  TEXT NOT NULL,
    "AVG"  REAL NOT NULL,
    "HR"  INTEGER NOT NULL,
    "RBI"  INTEGER NOT NULL,
    "SB"  INTEGER NOT NULL,
    "H" INTEGER NOT NULL,
    "OPS"  REAL NOT NULL,
    PRIMARY KEY("rank" AUTOINCREMENT)
)
'''

cursor.execute(sql)
con.commit() 
con.close()