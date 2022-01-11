#9개의 숫자 입력후 가장 큰수와 몇번째인지 구하기
X=list()#빈 리스트 생성
for _ in range (9):
    A=int(input())
    X.append(A)#빈리스트에 9개의 숫자 넣기
print(max(X))#리스트내의 최대값 구하기
B=(X.index(max(X)))#인덱스로 최대값 찾기
print(int(B)+1)#0번째부터 시작이 1더해줌

