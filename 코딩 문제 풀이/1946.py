#최고의 사원
T = int(input())
for i in range(T):
    N=float(input())
    result=[]
    if N%2==0:
        A=N//2
    else:
        A=(N//2)+1
    A=int(A)
    N=int(N)
    for j in range(N):
        x=list(map(int,input().split()))
        if (x[0] ==1) or (x[1] == 1):
            result.append(x)
        elif (x[0] <= A) and (x[1] <=A):
            result.append(x)
    print(len(result))


