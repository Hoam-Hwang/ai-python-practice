# day14_function_example3.py
# Day14 함수 심화 예제3 - 중첩 함수

def outer():
    print("외부 함수 실행")

    def inner():
        print("내부 함수 실행")

    inner()

outer()
