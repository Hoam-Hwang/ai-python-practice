# day14_function_example1.py
# Day14 함수 심화 예제1 - *args 사용법

def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))        # 출력: 6
print(add_all(4, 5, 6, 7, 8))  # 출력: 30
