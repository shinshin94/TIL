# OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다.
# 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

T=int(input())
for i in range(T):
    Y=list(input())
    end = 0
    total=0
    for v in Y:
        if v == 'O':
            total=(total+1)
            end+=total
        else:
            total=0
    print(end)