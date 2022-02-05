N,K=map(int,input().split())
A=[]
for i in range(N):
    x=int(input())
    A.append(x)
count = 0
for i in A[::-1]:
    count+= (K //i)
    K=K%i
print(count)