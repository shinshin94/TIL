#손익분기점 계산
A,B,C = map(int,input().split())
count=0
while True:
    if (A+(B*count)) < (C*count):
        print(count)
        break
    elif (C*count) > 2100000000:
        print('-1')
        break
    else:
        count+=1
