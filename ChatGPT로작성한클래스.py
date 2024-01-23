# Person 클래스 정의
class Person:
    # 생성자 메서드: id와 name을 초기화
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    # 정보 출력 메서드
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")


# Manager 클래스는 Person 클래스를 상속받음
class Manager(Person):
    # 생성자 메서드: id, name, title을 초기화하고, 부모 클래스의 생성자 호출
    def __init__(self, person_id, name, title):
        super().__init__(person_id, name)
        self.title = title

    # 정보 출력 메서드: 부모 클래스의 printInfo 호출 후 title 출력
    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


# Employee 클래스는 Person 클래스를 상속받음
class Employee(Person):
    # 생성자 메서드: id, name, skill을 초기화하고, 부모 클래스의 생성자 호출
    def __init__(self, person_id, name, skill):
        super().__init__(person_id, name)
        self.skill = skill

    # 정보 출력 메서드: 부모 클래스의 printInfo 호출 후 skill 출력
    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


# 10개의 Employee 인스턴스를 담은 리스트 생성 (샘플 코드)
employees = [
    Employee(1, "John", "Python"),
    Employee(2, "Jane", "Java"),
    Employee(3, "Mike", "C++"),
    Employee(4, "Emily", "JavaScript"),
    Employee(5, "Chris", "Data Science"),
    Employee(6, "Alice", "Machine Learning"),
    Employee(7, "Bob", "Web Development"),
    Employee(8, "Eva", "Database Management"),
    Employee(9, "Daniel", "Network Security"),
    Employee(10, "Sophia", "Artificial Intelligence")
]

# 각 Employee 인스턴스의 정보 출력 (샘플 코드)
for employee in employees:
    employee.printInfo()
    print("\n" + "="*20 + "\n")
