#더하기 사이클
x = int(input())
check=x
count=0
while True:
    front = check//10
    back = check%10
    sub = front + back
    subBack = sub%10
    check=str(back) + str(subBack)
    check=int(check)
    count += 1
    if check==x:
        print(count)
        break




