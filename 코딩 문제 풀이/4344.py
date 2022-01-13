# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

C=int(input())
for i in range(C):
    N=list(map(int,input().split()))
    B = (sum(N)-N[0])/N[0]
    count = 0
    for p in N[1:]:
        if p >B:
            count+=1
    end=(count/N[0])*100
    print("{:.3f} %%".format(end))



