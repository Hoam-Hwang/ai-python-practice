# day10_class_example2.py

# 부모 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 저는 {self.age}살 {self.name}입니다.")

# 자식 클래스 정의 (Person을 상속)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_id(self):
        print(f"학생 번호는 {self.student_id}입니다.")

# 인스턴스 생성 및 메서드 호출
s1 = Student("호암", 25, "2025001")
s1.introduce()  # Person 클래스의 메서드 사용
s1.show_id()    # Student 클래스의 메서드 사용
