# day06_list_practice2.py

fruits = []                                   # 빈 리스트 fruits를 만든다

for _ in range(3):                            # for _ in range(3): 3번 반복 
    fruit = input("과일 이름을 입력하세요: ") # 사용자에게 과일 이름을 입력받아 변수 fruit에 저장 
    fruits.append(fruit)                      # fruits 리스트에 fruit를 추가(append)

print(f"입력한 과일 리스트: {fruits}")        # 마지막에 입력한 과일 리스트를 출력  
    
# for _ in range(3):  
#  - range(3)은 0,1,2 총 3번 반복하는 의미  
#  - 반복할 때 변수 _는 '변수 사용 안 함'의 의미로,  
#    반복 횟수만 중요할 때 주로 사용함  
#  - 즉, 3번 반복하라는 뜻  
