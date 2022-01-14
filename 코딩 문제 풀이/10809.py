#알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오
AB=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
S=list(input())
for i in AB:
    AC=S.count(i)
    if AC > 1:
        BB=reversed(S)
        BB=list(BB)
        BB.remove(i)
        Si=reversed(BB)
        Si=list(Si)
        AT=Si.index(i)
        print(AT,end=' ')
    elif AC == 1:
        AT = S.index(i)
        print(AT, end=' ')
    else:
        print("-1",end=" ")
