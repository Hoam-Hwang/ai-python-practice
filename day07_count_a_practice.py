# day07_count_a_practice.py



text = input("입력하세요: ")
text = text.lower()                        # 변환된 값을 text에 다시 저장해야 함, 입력받은 문자열을 모두 소문자로 변환하여 대소문자 구분 없이 'a' 개수 세기
num_a = text.count('a')                    # 'a' 문자가 몇 번 나오는지 세기
print(f"결과: a는 {num_a}번 등장합니다.")  
