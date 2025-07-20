# day11_module_practice1.py

import random

numbers = [random.randint(1,10) for _ in range (5)]
print("랜덤 숫자 리스트:", numbers)
print("합:", sum(numbers))
print("평균:", sum(numbers) / len(numbers))
