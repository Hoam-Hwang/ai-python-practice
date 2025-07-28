# day16_list_comprehension_example2.py

# Day16 예제2 - 조건문이 포함된 리스트 컴프리헨션

# 1부터 20까지 중 짝수만 필터링해서 리스트로 만드는 예제입니다.

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)
