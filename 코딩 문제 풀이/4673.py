#10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력(양의 정수 n에 n의 각 자리수를 더하는 함수)
list1=[s+1 for s in range(10001)] #1 부터 10000까지 범위의 리스트 생성
Z=[]   #list1과 비교할 리스트 생성
def selfnum(num):  #비교할 리스트 Z에 추가할 수를 함수로 만듬
    X=int(num)#초기값을 다른곳에 저장
    Str=str(num) #문자열로 변환
    A=list(Str) #문자열로 바꾸어서 리스트로 들어가면서 분할됨
    B=len(A)#밑에 for문의 범위를 위해 구함
    for i in range (B):
        X+=int(A[i]) #초기값 X에 리스트의 숫자들이 더해져가는 공식
    return X #(다 더한 X값을 반환)

for y in range(1,10001):
    Z.append(selfnum(y))#함수에 1~10000까지 수를 넣고 돌려받은 값을 Z에 추가함
for i in range (10000): #숫자가 10000을 넘어가지 않으므로 10000번째까지만 지정
    if Z[i] in list1:
        list1.remove(Z[i]) #list1에서 리스트z와 겹치는 수를 제거
C = len(list1) #겹치는 수를 제거하고 남은 list1의 범위를 파악
for i in range (C): #범위 지정후 1줄씩 프린트트    print(list1[i])
