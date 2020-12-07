import sqlite3
db = sqlite3.connect("WebChatDB.db", isolation_level=None)

username = 'taro'
sql = 'SELECT passwd FROM usertable WHERE name =?'

cur = db.cursor()
cur.executemany(sql,username)
unko = cur.fetchone()
print(unko[1])

# クローズ
db.close()
