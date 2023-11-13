# DemoListTuple.py

# strA = "pythone is very prowerful"
# print(strA[0])
# print(strA[1])
# print(strA[0:6])
# print(strA[:6])
# print(strA[8:])
# print(strA)

colors = ["red", "blue", "green"]
print("1", len(colors))
print("2", type(colors))
colors.append("white")
colors.insert(1, "pink")
print("3",colors)

colors += "red"
print("4",colors)
print("5",colors.pop())
print("6",colors.pop())
print("7",colors)
colors.remove("red")
print("8",colors)
colors.extend(["black", "yellow","green"])
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)


#  디버깅할 때 중단점(Break Point)
for item in colors:
    print(10, item)


print("----- set 형식 -----")
a = {1,2,3,3}
b = {3, 4,4,5}
print(a)
print(type(b))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


print("----- Tuple 형식 -----")
tp = (10,20,30)
print(len(tp))
print(type(tp))

# 함수 정의
def calc(a,b):
    return a+b, a*b

# 호출
result = calc(3, 4)
print(result)
print(result[0])
print(result[1])

print("id:%s, name:%s" % ("kim","김유신"))
args = (5,6)
print(calc(*args))

print("----- 형식 변환 -----")
a = set((1, 2, 3))
#aa = set (4,5,6)
print(a)
b = list(a)
print(b)
b.append(4)
print(b)
print(type(b))

print("----- 형식 변환 -----")


