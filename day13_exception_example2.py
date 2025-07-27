# day13_exception_example2.py
# 여러 개 예외 처리 (ValueError, ZeroDivisionError)

try:
    a = int(input("a 입력: "))
    b = int(input("b 입력: "))
    result = a / b
    print("결과:", result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("정수가 아닙니다.")
