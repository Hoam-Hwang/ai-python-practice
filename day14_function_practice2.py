# day14_function_practice2.py
# Day14 함수 심화 응용문제2 - **kwargs로 키워드 인자 출력하기

def print_user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_user_info(name="호암", age=25, hobby="축구")
