#정수 입력 합 계산
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break