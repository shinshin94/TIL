#스택 연습
N=int(input())
stack=[]
for i in range (N):
    x=list(input().split())
    if x[0] == "push":
        stack.append(x[1])
    elif x[0] == "pop":
        if len(stack)==0:
            print(-1)
        else:
            stack.pop()
    elif x[0] == "size":
        print(len(stack))
    elif x[0] == "empty":
        if len(stack) ==0:
            print(1)
        else:
            print(0)
    elif x[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])