#1만들기
X=int(input())
count=0
if X!=1:
    while True:
        if X==1:
            break
        elif X%3==0:
            X=X//3
            count += 1
        elif X%2==0:
            X=X//2
            count += 1
        else:
            X-=1
            count += 1
print(count)