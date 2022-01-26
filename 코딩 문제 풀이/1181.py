X=int(input())
Y=[]
for i in range(X):
    s=input()
    Y.append(s)
Z=set(Y)
A=list(Z)
A.sort()
A.sort(key=len)
for i in A:
    print(i)