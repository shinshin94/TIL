N=list(map(int,input().split()))
M=[]
def cou(i):
    x=2
    for x in range(i):
        if (i % x) ==0:
            break
        else:
            continue
        M.append(i)
for z in N:
    if z == 1:
        continue
    else:
        cou(z)
print(len(M))


