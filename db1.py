#db1.py
import sqlite3

#메모리에서 작업
# 연결객체 리턴받기
con = sqlite3.connect(":memory:")
# 커서객체 리턴
cur = con.cursor()

#테이블 구조(자료구조 생성)
cur.execute("create table PhoneBook(name text, phoneNum text);")

#데이터 1건 입력
cur.execute("insert into PhoneBook values('홍길동','010-111');")
#cur.execute("insert into PhoneBook values('홍길동','010111');")

#입력 파라메터 처리
name = "전우'치"
phonenumber = "010-123"
cur.execute("insert into PhoneBook values(?, ?);", (name, phonenumber))


#N건 입력
datalist =(("박문수","010-333"), ("김길동","010-567"))
cur.executemany("insert into PhoneBook values(?, ?);", datalist)


#검색
cur.execute("select * from phonebook;")
# for row in cur:
#     print(row)

print("----------- fetchone()1 -----------")
print(cur.fetchone())
print("----------- fetchone()2 -----------")
print(cur.fetchone())
print("----------- fetchmany(2) -----------")
print(cur.fetchmany(2))
cur.execute("select * from phonebook;")
print("----------- fetchall() -----------")
print(cur.fetchall())
