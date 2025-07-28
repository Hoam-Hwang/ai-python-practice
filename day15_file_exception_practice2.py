# day15_file_exception_practice2.py

# 파일 내 숫자들의 평균을 계산하고 출력 (예외 처리 포함)

# 이 문제는 숫자의 총합뿐 아니라 개수를 세어 평균까지 계산합니다.
# 잘못된 줄은 ValueError로 무시됩니다.

filename = input("읽을 파일명을 입력하세요: ")

try:
    total = 0
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            try:
                number = int(line.strip())
                total += number
                count += 1
            except ValueError:
                continue
    if count > 0:
        average = total / count
        print(f"총합: {total}, 평균: {average:.2f}")
    else:
        print("유효한 숫자가 없습니다.")
except FileNotFoundError:
    print(f"파일 '{filename}' 을 찾을 수 없습니다.")
