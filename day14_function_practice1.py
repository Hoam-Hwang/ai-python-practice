# day14_function_practice1.py
# Day14 함수 심화 응용문제1 - *args 평균 구하기

def average(*args):
    total = sum(args)
    count = len(args)
    if count == 0:
        return 0
    return total / count

print(average(1, 2, 3, 4))     # 출력: 2.5
