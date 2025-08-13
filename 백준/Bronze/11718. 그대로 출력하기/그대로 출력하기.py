while True:
    try:
        print(input())
    except EOFError:
        break #try-except를 이용한 예외처리
        