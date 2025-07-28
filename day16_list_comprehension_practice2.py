# day16_list_comprehension_practice2.py

# Day16 응용문제2 - 구구단 2단부터 9단까지의 결과를 리스트 컴프리헨션으로 생성

# 각 곱셈 결과를 문자열로 저장 (예: "2x1=2", ..., "9x9=81")

gugudan = [f"{i}x{j}={i*j}" for i in range(2, 10) for j in range(1, 10)]
print(gugudan)
