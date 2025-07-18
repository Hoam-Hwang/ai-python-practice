# day05_count_sum_practice.py

num = int(input("숫자를 입력하세요: "))  # 사용자에게 숫자 입력받아 정수로 변환
i = 1                                    # 더하기 시작할 숫자 초기화
total = 0                                # 합을 저장할 변수 초기화

while i <= num:                          # i가 num 이하일 동안 반복
    total += i                           # total에 i 더하기 (total = total + i)
    i += 1                               # i를 1씩 증가시켜 다음 숫자로 이동

print(f"1부터 {num}까지의 합은 {total} 입니다.")  # 결과 출력 (f-string 사용)

