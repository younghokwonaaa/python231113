#DemoRE.py
#정규 표현식을 사용하는 경우
import re

print("----- search (공백 추가시 조회가능)-----")
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

# print("----- match (공백 추가시 조회불가)-----")
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result = re.search("\d{4}", "올202해는 2023년")
print(result.group())

result = re.search("\d{5}", "우리12 동네는 51200")
print(result.group())


strA = """다중라인
으로 

문자열저장"""

c = re.compile("^.+")
result = c.findall(strA, re.MULTILINE)
print(result)


#p = re.compile("^python\s\w+", re.MULTILINE)
p = re.compile("^.+", re.MULTILINE)

data = """python one
 
life is too short
python two

you need python
python three"""

print(p.findall(data))
