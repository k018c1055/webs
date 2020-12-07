import sqlite3
db = sqlite3.connect("WebChatDB.db", isolation_level=None)
c = db.cursor()

#usertable作成..
sql = """
    CREATE TABLE usertable (
        name VARCHAR(30),
        passwd VARCHAR(30)
    );
"""
c.execute(sql)

sql = 'INSERT INTO usertable (name, passwd) VALUES (?,?)'
data = [('taro',1111),
            ('yamada',2222)]
c.executemany(sql, data)


#room1log作成
sql = """
    CREATE TABLE room1log (
        name VARCHAR(30),
        chatlog VARCHAR(300),
        time VARCHAR(12)
    );
"""
c.execute(sql)

sql = 'INSERT INTO room1log (name, chatlog,time) VALUES (?,?,?)'
data = [('taro','おはよう','202011301352'),
            ('yamada','おはようございます。','202011301402')]
c.executemany(sql, data)


# コミット
db.commit()
    
# データ（レコード）取得
sql = 'SELECT * FROM usertable'
print('------[usertable]------')
for row in c.execute(sql):
    print(row)
print('------[room1log]------')
sql = 'SELECT * FROM room1log'
for row in c.execute(sql):
    print(row)

# クローズ
db.close()


""" username = 'taro'
sql = 'SELECT passwd FROM usertable WHERE name =?'
print(c.execute(username)) """
