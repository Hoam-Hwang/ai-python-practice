# day15_file_exception_example1.py

# Day15 예제1 - 파일이 없을 때 예외 처리 (FileNotFoundError)

# 이 예제는 존재하지 않는 파일을 열려고 할 때 발생하는 FileNotFoundError를 처리하는 방법을 보여줍니다.
# finally 블록은 성공 여부와 관계없이 항상 실행됩니다.

filename = "nonexistent.txt"

try:
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"파일 '{filename}' 이 존재하지 않습니다.")
finally:
    print("파일 처리 시도 완료.")
