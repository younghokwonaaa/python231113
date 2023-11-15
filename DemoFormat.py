#DemoFormat.py

for i in range(1, 11):
    URL = "http://multi.com/?page="+str(i)
    print(URL)

print("--------- 숫자 출력 ---------")
for x in range(1, 6):
    print(x, "*", x , "=", x*x)

print("--------- 오른쪽 정렬 ---------")
for x in range(1, 6):
    print(x, "*", x , "=", str(x*x).rjust(3))

print("--------- 0으로 채우기 ---------")
for x in range(1, 6):
    print(x, "*", x , "=", str(x*x).zfill(5))


print("--------- 파일 처리 ---------")
#파일 쓰기
# #f = open("c:\\work\\test.txt", "at", encoding="utf-8")
# f = open(r"c:\work\test.txt", "wt", encoding="utf-8")
# #f.write("첫번째 라인\n두번째 라인\n세번째 라인\n")
# f.write("""첫번째 라인1
# 두번째 라인2
# 세번째 라인3
# test 입니다.""")
# f.close()


print("--------- 파일 등록 ---------")
#파일에 첨부
#f = open("c:\\work\\test.txt", "at", encoding="utf-8")
f = open(r"c:\work\test.txt", "a+", encoding="utf-8")
#f.write("첫번째 라인\n두번째 라인\n세번째 라인\n")
f.write("추가로 첨부하기\n")
f.close()


print("--------- 파일 조회 read ---------")
#파일 읽기
#f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
f = open(r"c:\work\test.txt", "r", encoding="utf-8")
print(f.read())
# 다시 처음으로 리셋
print("--------- 파일 조회 readlines ---------")
f.seek(0)
rresult = f.readlines()
for item in rresult:
    print(item, end="")


print("--------- 파일 조회 readline ---------")
#다시 처음으로 
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
f.close()

print("--------- 서식지정 ---------")
#서식 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(1155000))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
