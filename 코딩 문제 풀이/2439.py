#우측 별찍기
X = int(input())
i=1
for i in range(X+1):
    print(" "*(X),end="")
    print("*"*(i))
    X-=1