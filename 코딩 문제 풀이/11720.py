#숫자 갯수를 입력 받고 숫자가 각자릿수의 숫자의 합 구하기
import random
A = int(input("숫자 갯수를 입력하시오 : "))
D =""
for x in range(A):
    X=random.randint(0,9)
    X=str(X)
    print(X,end="")
    D+=X
print()
B=(0*(D.count("0")))+(1*(D.count("1")))+(2*(D.count("2")))+(3*(D.count("3")))+(4*(D.count("4")))+(5*(D.count("5")))+(6*(D.count("6")))+(7*(D.count("7")))+(8*(D.count("8")))+(9*(D.count("9")))
print(B)
