# db2.py 
import sqlite3

#연결객체(실제 파일에 저장) 
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체
cur = con.cursor() 
#테이블을 생성(테이블이 없는 경우?)
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")
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
cur.execute("select * from PhoneBook order by name;")
for row in cur:
    print(row)

#작업 정상적으로 완료
con.commit() 



