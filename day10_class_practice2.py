# day10_class_practice2.py

class Car:
    def __init__(self, brand, year):
        self.brand = brand     # 자동차 브랜드
        self.year = year       # 제조년도
 
    def show_info(self):
        print(f"브랜드 {self.brand}, 제조년도: {self.year}")

class ElectricCar(Car):              # Car 클래스로부터 상속
    def __init__(self, brand, year, battery):
        super().__init__(brand,year)   # 부모 클래스 생성자 호출
        self.battery = battery       # 추가 속성: 배터리 용량

    def show_battery(self):
        print(f"배터리 용량: {self.battery}")

# 사용 예시
my_car = ElectricCar("Tesla", 2022, "85kWh")
my_car.show_info()       # 출력: 브랜드: Tesla, 제조년도: 2022
my_car.show_battery()    # 출력: 배터리 용량: 85kWh
