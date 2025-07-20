# day12_file_practice1.py

# 사용자로부터 이름과 나이 입력받기
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")

# user_info.txt 파일에 저장
with open("user_info.txt", "w", encoding="utf-8") as f:
    f.write(f"이름: {name}\n")
    f.write(f"나이: {age}\n")

# 저장된 파일 읽어서 출력
with open("user_info.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
