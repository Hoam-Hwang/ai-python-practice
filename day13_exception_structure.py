# day13_exception_structure.py
# 예외 처리 기본 구조 (try / except / else / finally)

try:
    num = int(input("숫자를 입력하세요: "))
    print(f"입력한 숫자: {num}")
except ValueError:
    print("유효하지 않은 숫자입니다.")
else:
    print("정상적으로 입력되었습니다.")
finally:
    print("프로그램 종료")
