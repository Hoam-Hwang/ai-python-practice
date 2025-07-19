# day09_function_practice2.py

def find_max(a, b, c):
    if a >= b and a>=c:
        return a
    if b >= a and b >= c:
        return b
    else:
        return c
    
# 사용자 입력 받기
a = int(input("첫 번째 숫자: "))
b = int(input("두 번째 숫자: "))
c = int(input("세 번째 숫자: "))

result = find_max(a, b, c)
print(f"가장 큰 수는 {result}입니다.")

# def find_max(a, b, c):
#    return max(a, b, c)
