# day09_function_practice1.py

def calculator(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
op = input("연산 기호(+ - * /): ")

result = calculator(a,b,op)
print(f"결과는 {result}입니다.")

'''
def calculator():
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))
    op = input("연산 기호(+ - * /): ")
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b

result = calculator()
print(f"결과는 {result}입니다.")
'''
