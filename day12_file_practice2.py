# day12_file_practice2.py

# numbers.txt 파일에 1부터 10까지 저장
with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")

# numbers.txt 파일 읽어서 합 계산
total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        total += int(line.strip())

print(f"총합: {total}")
