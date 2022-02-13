#빈칸 채우기
N,M = map(int,input().split())
A=[]
C=[0]*M
ROW=0
for i in range(N):
    B=list(input().split())
    if B.count('X') >=1:
        pass
    else:
        ROW+=1
    for j in range(M):
        if B[j] == 'X':
            C[j] = 'X'
print(C)
COL=C.count(0)
print(max(ROW,COL))
