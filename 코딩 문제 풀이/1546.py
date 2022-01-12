#기말 점수 조작( 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다)
X=int(input())
A= list(map(int,input().split()))
M=max(A)
D=0
for i in A:
    i=i/M*100
    D+=i
end=D/3
print("%f"%end)
