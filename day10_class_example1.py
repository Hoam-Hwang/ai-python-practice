# day10_class_example1.py

# 간단한 사람 클래스 정의
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 저는 {self.name}이고, 나이는 {self.age}살 입니다.")

p1 = Person("호암", 25)
p1.introduce()
