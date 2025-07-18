# day07_reverse_string_practice.py

word = input("입력하세요: ")
print(word[::-1])

'''
word = input("입력하세요: ")
reversed_word = ''.join(reversed(word))
# 1) reversed(word): 문자열 'word'를 거꾸로 뒤집은 iterator(반복자)를 만듦
# 2) ''.join(...): 빈 문자열 ''을 기준으로 iterator의 각 문자들을 연결하여 새로운 문자열 생성
print(reversed_word)
'''
