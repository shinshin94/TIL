T = int(input())
for i in range(T):
    x=input()
    if x.count("(") == x.count(")"):
        if (x[0]=="(") and (x[-1]==")"):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")