# day05_while_input_example.py

while True:
    word = input("그만하려면 '종료'라고 입력하세요: ")
    if word == "종료":
        print("프로그램을 종료합니다.")
        break
    print("입력한 단어:", word)

# while True는 무한 루프 (끝없이 반복)
# 내부에서 if 조건을 걸어 break로 빠져나오는 방식으로 사용
