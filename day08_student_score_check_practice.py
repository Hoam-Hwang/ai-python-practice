# day08_student_score_check_practice.py

students = {
    "민기": 100,
    "승완": 90,
    "민준": 80
}

name = input("학생의 이름을 입력하세요: ")

if name in students:
    print(f"{name}의 점수는 {students[name]}점 입니다.")
else:
    print("학생 정보가 없습니다.")
