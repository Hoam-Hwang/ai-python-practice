# day15_file_exception_example2.py

# Day15 예제2 - 파일에서 숫자만 읽고 합계 구하기 (ValueError 예외 처리 포함)

# 이 예제는 텍스트 파일에서 숫자만 읽어와 합계를 구하고,
# 숫자가 아닌 값이 있는 줄은 무시하도록 ValueError 예외 처리를 포함합니다.

filename = "numbers.txt"

try:
    total = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            try:
                number = int(line)
                total += number
            except ValueError:
                print(f"무시된 줄: '{line}' (숫자가 아님)")
    print(f"총합: {total}")
except FileNotFoundError:
    print(f"파일 '{filename}' 을 찾을 수 없습니다.")
