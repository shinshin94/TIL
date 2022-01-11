#주어진 두 수에 따른 사분면 출력
X=int(input())
if X>1000 or X<-1000 or X == 0 :
    exit(print("X>1000,X<-1000,X == 0 이외로 해주십죠.")) #범위 넘어가면 닫음
Y=int(input())
if Y>1000 or Y<-1000 or Y==0 :
    exit(print("Y>1000,Y<-1000,Y == 0 이외로 해주십죠."))
Q = [X,Y]#리스트로 묶는다
if (Q[0] > 0 and Q[1] > 0): #비교
    print(Q,"Quadrant1 입니다")
    if (Q[0] < 0 and Q[1] > 0):
        print(Q,"Quadrant2 입니다")
        if (Q[0] < 0 and Q[1] < 0):
            print(Q,"Quadrant3 입니다")
        else:
            print(Q, "Quadrant4 입니다")