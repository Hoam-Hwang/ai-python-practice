# day15_file_exception_practice3.py

# 사용자 입력으로 숫자 파일에 추가하는 프로그램 (쓰기 모드 + 예외 처리)

filename = "numbers.txt"

try:
    number = int(input("추가할 숫자를 입력하세요: "))
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{number}\n")
    print(f"{number}가 {filename}에 추가되었습니다.")
except ValueError:
    print("숫자가 아닌 값이 입력되었습니다.")
except Exception as e:
    print("알 수 없는 오류 발생:", e)
