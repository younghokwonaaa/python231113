#부모 클래스
class Person(object):# ojbect 있으나 없으나 동일하다.
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
            self.phoneNumber))
    
    def working(self):
        print("현재 작업중...")
    def coding(self):
        print("현재 코딩중...")

# 자식 클래스
class Student(Person):
    # 멤버변수 추가(덮어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        # 부모클래스의 name, phoneNumber를 초기화 한다.
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID

    #상속받아서 덮어쓰기(재정의, override)
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, 
            self.phoneNumber))
        print("Info(학과:{0}, 학번: {1})".format(self.subject, 
            self.studentID))
        print("Info(Name:{0}, Phone Number: {1}, 학과:{2}, 학번: {3}))".format(self.name, 
            self.phoneNumber, self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터학과", "201234")
# print(p.__dict__)
# print(s.__dict__)
p.printInfo()
s.printInfo()
s.working()
s.coding()


