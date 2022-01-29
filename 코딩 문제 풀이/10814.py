#나이순 정렬
N = int(input())
x=[]
for _ in range(N):
    y,z=input().split()

    x.append([y,z])
print(x)
x.sort(key=lambda x:(x[0],x[1]))

# for i in range(N):
#     print(x[i])
