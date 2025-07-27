# day14_function_practice3.py
# Day14 함수 심화 응용문제3 - 중첩 함수에 매개변수 전달하기

def outer(msg):
    print("외부 함수:", msg)

    def inner():
        print("내부 함수 호출")

    inner()

outer("안녕하세요")
