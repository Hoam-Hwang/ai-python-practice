# day05_countdown_practice.py

count = int(input("시작할 숫자를 입력하세요: "))  # 숫자 입력받고 정수로 변환
while count >0:                                   # count가 1 이상일 때 반복
    print(count)                                  # 현재 count 출력
    count -= 1                                    # count를 1 줄임
print("발사!")                                    # 반복 끝나면 "발사" 출력
