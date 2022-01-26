N=int(input())
A=2
B=1
while True:
    if N==B:
        break
    elif N%A==0:
        print(A)
        N=N//A
    else:
        A+=1

