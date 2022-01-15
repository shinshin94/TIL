#문자열 반복
Go = int(input())
for i in range(Go):
    X,Ch=list(map(str,input().split()))
    X=int(X)
    for Y in Ch:
        print(Y*X,end='')
    print()