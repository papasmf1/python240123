# db1.py 
import sqlite3

#연결객체 
con = sqlite3.connect(":memory:")
#커서객체
cur = con.cursor() 
#테이블을 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('김길동', '010-222');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)


