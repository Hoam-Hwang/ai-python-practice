# day15_file_exception_practice1.py

# Day15 응용문제1 - 사용자 입력 기반 숫자 파일 합계 계산

# 이 문제는 사용자가 직접 파일명을 입력하면 해당 파일을 열고 숫자만 읽어 합계를 계산합니다.
# 없는 파일일 경우 FileNotFoundError를 처리하고, 숫자가 아닌 줄은 무시합니다.

filename = input("읽을 파일명을 입력하세요: ")

try:
    total = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            try:
                total += int(line.strip())
            except ValueError:
                continue
    print(f"{filename} 파일 내 숫자의 합: {total}")
except FileNotFoundError:
    print(f"파일 '{filename}' 을 찾을 수 없습니다.")
