# T횟수 만큼 계산 결과 출력
T = int(input())
for x in range(T):
    A,B = map(int,input().split())
    sub=A+B
    print('Case #%s: %s '%(x+1,sub))