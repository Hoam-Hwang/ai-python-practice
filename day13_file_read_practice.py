# day13_file_read_practice.py
# 파일 읽기와 예외 처리 (파일이 없을 때 처리하기)

filename = input("파일명을 입력하세요: ")

try:
    with open(filename, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    print("파일 내용:")
    print(content)
except FileNotFoundError:
    print("파일이 없습니다.")
