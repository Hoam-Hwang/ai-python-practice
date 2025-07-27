# day13_exception_example1.py
# 0으로 나누기 예외 처리 (ZeroDivisionError)

try:
    a = int(input("숫자 a: "))
    b = int(input("숫자 b: "))
    print(f"a / b = {a / b}")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
