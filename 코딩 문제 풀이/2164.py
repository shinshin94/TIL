#버리고 밑으로 반복
# def egg():
#     if len(Y) == 1:
#         print(Y[0])
#     else:
#         Z = []
#         Z.append(Y[1])
#         del Y[0]
#         Y = Y + Z
#     egg()

X=int(input())
Y = []
for i in range(1,X+1):
    Y.append(i)
while True:
    if len(Y) == 1:
        print(Y[0])
        break
    else:
        Z = Y[1]
        Y.append(Z)
        del Y[0:2]
