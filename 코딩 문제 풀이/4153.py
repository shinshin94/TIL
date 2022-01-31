#직각삼각형
while True:
    x,y,z=map(int,input().split())
    if (x==0 and y==0 and z==0):
        break
    x=x**2;y=y**2;z=z**2
    if ((x+y==z) or (x+z==y)):
        print("right")
    else:
        print("wrong")


