#입력받은것의 아스키코드 출력
X=input()
if isinstance(X, int) == True:
    print(chr(X))
else:
    print(ord(X))