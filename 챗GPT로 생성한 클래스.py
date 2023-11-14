class Person:
    def __init__(self, id, title):
        """
        사람을 표현하는 클래스입니다.

        :param id: 사람의 고유 식별자
        :param title: 사람의 직업이나 호칭
        """
        self.id = id
        self.title = title

    def printInfo(self):
        """
        사람의 정보를 출력하는 메서드입니다.
        """
        print(f"아이디: {self.id}, 직업: {self.title}")


class Manager(Person):
    def __init__(self, id, title, skill):
        """
        매니저를 표현하는 클래스입니다. Person 클래스를 상속받습니다.

        :param id: 매니저의 고유 식별자
        :param title: 매니저의 직업이나 호칭
        :param skill: 매니저의 특기나 능력
        """
        super().__init__(id, title)
        self.skill = skill

    def printInfo(self):
        """
        매니저의 정보를 출력하는 메서드입니다.
        """
        super().printInfo()
        print(f"특기: {self.skill}")


class Employee(Person):
    def __init__(self, id, title, role):
        """
        직원을 표현하는 클래스입니다. Person 클래스를 상속받습니다.

        :param id: 직원의 고유 식별자
        :param title: 직원의 직업이나 호칭
        :param role: 직원의 역할이나 일
        """
        super().__init__(id, title)
        self.role = role


# 아래는 각 클래스와 메서드를 사용하는 예시입니다.

# 예시 1
person1 = Person(1, "존 도우")
person1.printInfo()

# 예시 2
manager1 = Manager(2, "앨리스 스미스", "리더십")
manager1.printInfo()

# 예시 3
employee1 = Employee(3, "밥 존슨", "개발자")
employee1.printInfo()

# 예시 4
person2 = Person(4, "제인 도우")
person2.printInfo()

# 예시 5
manager2 = Manager(5, "찰리 브라운", "커뮤니케이션")
manager2.printInfo()

# 예시 6
employee2 = Employee(6, "데이비드 밀러", "디자이너")
employee2.printInfo()

# 예시 7
person3 = Person(7, "에바 그린")
person3.printInfo()

# 예시 8
manager3 = Manager(8, "프랭크 화이트", "프로젝트 관리")
manager3.printInfo()

# 예시 9
employee3 = Employee(9, "그레이스 터너", "분석가")
employee3.printInfo()

# 예시 10
person4 = Person(10, "해리 블랙")
person4.printInfo()

p1 = Person(100, "개발자")
p1.printInfo()