# 별찍기
def astar(x):
    if x<=1:
        return 1
    return x*astar(x-1)

a=int(input())
print(astar(a))