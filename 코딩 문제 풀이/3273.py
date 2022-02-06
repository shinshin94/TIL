#두개의 합
N=int(input())
cal=list(map(int,input().split()))
X=int(input())
result=0
for i in range(N):
    for j in range(N):
        if cal[i]+cal[j]==X:
            result+=1
print(result//2)
