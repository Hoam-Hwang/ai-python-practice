# day13_division_practice.py
# [연습] 반복문과 예외 처리로 나누기 계산기 만들기

while True:
    a = input("첫 번째 숫자 입력 (종료하려면 q): ")
    if a.lower() == 'q':
        print("프로그램 종료")
        break

    b = input("두 번째 숫자 입력 (종료하려면 q): ")
    if b.lower() == 'q':
        print("프로그램 종료")
        break

    try:
        num1 = int(a)
        num2 = int(b)
        result = num1 / num2
    except ValueError:
        print("정수를 입력해주세요.")
        continue
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
        continue
    else:
        print(f"{num1} / {num2} = {result}")
