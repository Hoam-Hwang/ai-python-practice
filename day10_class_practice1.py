# day10_class_practice1.py

class Rectangle:
      # 클래스 생성자에서 받은 값을 객체 속성으로 저장
      # self.width, self.height는 객체마다 따로 저장되는 값
    def __init__(self, width, height):
        self.width = width    # 매개변수 width 값을 객체의 width 속성에 저장
        self.height = height  # 매개변수 height 값을 객체의 height 속성에 저장

    def get_area(self):
        return self.width * self.height
         # self.width, self.height는 각각 객체가 가진 속성 값

    def get_perimeter(self):
        return (self.width + self.height) *2

# 사용자 입력
w = int(input("가로 길이를 입력하세요: "))
h = int(input("세로 길이를 입력하세요: "))

# Rectangle 클래스 객체 생성
# w와 h가 각각 width, height 매개변수로 전달됨
rect = Rectangle(w, h)
print(f"사각형의 넓이는 {rect.get_area()}입니다.")
print(f"사각형의 둘레는 {rect.get_perimeter()}입니다.")
