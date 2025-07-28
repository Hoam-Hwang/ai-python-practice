# day16_list_comprehension_example3.py

# Day16 예제3 - 중첩 for문을 사용하는 리스트 컴프리헨션

# 이 예제는 1~3과 A~C를 조합하여 ['1A', '1B', ..., '3C'] 형태의 리스트를 만듭니다.

pairs = [str(x) + y for x in range(1, 4) for y in ['A', 'B', 'C']]
print(pairs)
