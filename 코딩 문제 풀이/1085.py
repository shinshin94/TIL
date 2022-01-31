#직사각형 탈출
x,y,w,h =map(int,input().split())
a=[]
a.append(abs(0-x))
a.append(abs(0-y))
a.append(abs(0-w))
a.append(abs(0-h))
a.append(abs(x-w))
a.append(abs(y-h))
print(min(a))