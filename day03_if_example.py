# day03_if_example.py

score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A등급입니다.")
elif score >= 80:
    print("B등급입니다.")
elif score >= 70:
    print("C등급입니다.")
else:
    print("재도전이 필요합니다.")
