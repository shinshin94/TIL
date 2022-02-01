#직사각형 만들기
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=list(map(int,input().split()))
a=x[0]+x[1]
b=y[0]+y[1]
c=z[0]+z[1]
if a>b and a>c:
    y=y[0]-z[0],y[1]-z[1]
    print(x[0]+abs(y[0]),x[1]-abs(y[1]))
elif b>a and b>c:
    x=x[0]-z[0],x[1]-z[1]
    print(y[0]+abs(x[0]),y[1]-abs(x[1]))
else:
    x=x[0]-y[0],x[1]-y[1]
    print(z[0]+abs(x[0]),z[1]-abs(x[1]))

