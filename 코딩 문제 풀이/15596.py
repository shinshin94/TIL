# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
def solve(a):
    ans=0
    for i in (a):
        ans+=i
    return ans
n=map(int,input().split())
print(solve(n))

