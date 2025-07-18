# day08_add_student_practice.py

students = {}                             # 빈 딕셔너리를 만든다.

while True:                               # 무한 반복문을 시작한다.
    name = input("학생 이름 입력: ")      # 사용자에게 이름을 입력받는다.
    if name == "끝":                      # "끝"이면 break로 반복문을 종료한다.
        break
    score = int(input("점수 입력: "))     # 이름이 "끝"이 아니면 점수를 입력받고 int()로 정수 변환한다.
    students[name] = score                # 딕셔너리에 추가한다.

print(students)                           # 반복이 끝나면 print(students)로 전체 딕셔너리를 출력한다.
