from config import *
from sqlite3 import connect

con = connect(DATABASE)
con.execute(
    "CREATE TABLE IF NOT EXISTS memo "
    "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
    "time TEXT,"
    "text TEXT)"
)

con.commit()
con.close()