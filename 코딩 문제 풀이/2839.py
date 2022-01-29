# 설탕 포대 적게 들기
N = int(input())
A= N//5
while True:
    siba= N-(A*5)
    if siba == 0:
        print(A)
        break
    suba=siba%3
    if suba == 0:
        print(A+(siba//3))
        break
    else:
        if A==0:
            continue
        else:
            A-=1

