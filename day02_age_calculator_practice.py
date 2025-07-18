# day02_age_calculator_practice.py

name = input("이름이 뭐야? ")
birth_year = int(input("몇년도에 태어났어? "))
print(name + "님은 2025년에 만 " + str(2025 - birth_year) +"입니다.")

#print(f"{name}님은 2025년에 만 {2025 - birth_year}입니다.")
# input() 함수는 사용자로부터 입력을 받을 때 사용해요.
# 입력된 값은 기본적으로 문자열(string)로 저장됩니다.
# 숫자 계산을 하려면 int() 같은 변환 함수가 필요해요.
# int() 함수는 문자열을 정수(integer)로 변환할 때 사용해요.
# 예를 들어, input()으로 받은 숫자 형태의 문자열을 숫자로 바꿀 때 꼭 필요합니다.
