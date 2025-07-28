# day16_list_comprehension_practice1.py

# Day16 응용문제1 - 문자열 리스트에서 숫자만 추출하여 정수 리스트 만들기

# ['10', 'abc', '25', '3.14', '42'] 에서 숫자인 것만 골라 정수 리스트로 만들기

data = ['10', 'abc', '25', '3.14', '42']
numbers = [int(x) for x in data if x.isdigit()]
print(numbers)  # 결과: [10, 25, 42]
