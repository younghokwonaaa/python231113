 # DemoStr.py
print(dir(str))

strA = "python is very prowerful"
strB = "피이썬은 강력해"
print("len(strA) : ", len(strA))
print("len(strB) : ", len(strB))
print("strA.capitalize() : ", strA.capitalize())
print("strA.count('p') : ", strA.count("p"))
print("strA.startswith('py') : ", strA.startswith("py"))
print("strA.endswith('ful') : ", strA.endswith("ful"))

print("-------- 알파벳과 숫자로 구성 --------")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

print("-------- 문자열 처리 구성 --------")
data = "<<< spam and ham >>>"
result  = data.strip("<>")
print(data)
print(result)
result = result.replace("spam", "spam egg")
print("변환 결과")
print(result)
result = "spam::gee::ham"
#구분자를 지정하는 경우
lst = result.split("::")
print(lst)
print("--- 다시 합치기 ---")
print(":)".join(lst))

#반복 문자열 생성
names = ["전우치","이순신","박문수"]
for name in names:
    print("="*40)
    print("안녕하세요 {0}님 초겨울 입니다.".format(name))
print("="*40)