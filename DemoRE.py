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



