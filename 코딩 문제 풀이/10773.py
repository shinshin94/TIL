#제로 스택
K = int(input())
stack=[]
res=0
for _ in range(K):
    x=int(input())
    if x==0:
        stack.pop()
    else:
        stack.append(x)
for i in range(len(stack)):
    res+=stack[i]
print(res)
