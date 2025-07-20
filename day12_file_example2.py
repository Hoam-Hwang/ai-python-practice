# day12_file_example2.py

# 여러 줄을 리스트로 저장 후 파일에 쓰기
lines = ["Apple\n", "Banana\n", "Cherry\n"]

with open("fruits.txt", "w") as f:
    f.writelines(lines)

# 한 줄씩 읽어서 출력
with open("fruits.txt", "r") as f:
    for line in f:
        print("읽은 줄:", line.strip())
