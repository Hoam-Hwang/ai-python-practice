# day05_password_check_practice.py

while True:                                     # 무한 반복 시작 
    password = input("비밀번호를 입력하세요: ") # 사용자로부터 비밀번호 입력 받음
    if password == "ai1234":                    # 입력한 비밀번호가 맞으면
        print("로그인 성공")                    # 로그인 성공 메시지 출력
        break                                   # 반복문 종료해서 프로그램 종료
    print("틀렸습니다.")                        # 틀리면 메시지 출력하고 다시 반복
    
