# day12_file_example1.py

# 파일에 내용 쓰기
with open("sample.txt", "w") as f:
    f.write("첫 번째 줄\n")
    f.write("두 번째 줄\n")

# 파일에서 내용 읽기
with open("sample.txt", "r") as f:
    content = f.read()
    print("파일 내용:\n", content)
