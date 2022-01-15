# X,Y =map(str,input().split())
# def cou(X,Y):
#     se=3
#     for i in range(se, 0, -1):
#         if int(X[se-1]) > int(Y[se-1]):
#             print(X[i - 1], end='')
#         elif int(X[se-1]) == int(Y[se-1]):
#             se-1
#             cou(X,Y)
# cou(X,Y)

# for i in range(3,0,-1):
#     if int(X[2]) > int(Y[2]):
#         print(X[i-1],end='')
#     elif int(X[2]) == int(Y[2]):
#         for z in range(2,0,-1):
#             if int(X[1]) > int(Y[1]):
#                 print(X[i-1], end='')
#             elif int(X[1]) == int(Y[1]):
#                 for q in range(1, 0, -1):
#                     if int(X[0]) > int(Y[0]):
#                         print(X[i-1], end='')
#                     else:
#                         print(print(X[i-1], end=''))

X, Y = input().split()
X = int(X[::-1])
Y = int(Y[::-1])

if X > Y:
    print(X)
else :
    print(Y)


