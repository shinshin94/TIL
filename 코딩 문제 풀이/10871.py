# 정수를 입력받고 비교하여 작을시 출력
N,X =map(int,input().split())
A=list(map(int,input().split()))

for i in range(N):
    if A[i]< X :
        print(A[i],end=" ")