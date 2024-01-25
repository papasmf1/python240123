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
#입력 파라메터 처리 
name = "전우치"
phoneNum = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))
#여러개 행을 입력 
datalist = (("이순신","010-444"), ("박문수","019-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())


