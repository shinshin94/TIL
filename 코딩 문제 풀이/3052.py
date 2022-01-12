#42로 나누고 나머지가 다른 갯수를 구하기
X=[]
for _ in range(10):
    A=int(input())
    B=A%42
    if B not in X:
        X.append(B)
print(len(X))