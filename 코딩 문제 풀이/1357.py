#숫자 뒤집기
def Rev(a):
    b=str(a)
    c=b[::-1]
    c=int(c)
    return c

X,Y=map(int,input().split())
print(Rev(Rev(X)+Rev(Y)))