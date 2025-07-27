# day14_function_example2.py
# Day14 함수 심화 예제2 - **kwargs 사용법

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="호암", age=30, job="학생")
