# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    # 초기화
    def __init__(self, id, name, balance):        
        # self.id = id
        # self.name = name 
        # self.balance = balance 
        # 이름을 숨김
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    #입금
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #결과를 문자로 리턴
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id,
            self.__name, self.__balance)
    
    #print 메서드 생성
    def output1(self):
        print(self.__id)
    def output2(self):
        print(self.__id, self.__name)
    def output3(self):
        print(self.__id, self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)
print(account1)
#print(account1.__name) 접근 불가능
#테스트코드(백도어)
account1._BankAccount__balance = 15000000
print(account1._BankAccount__balance)
account1.output1()
account1.output2()
account1.output3()

