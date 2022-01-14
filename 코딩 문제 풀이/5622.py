# #전화 걸기 알파벳으로 전화걸기
# Y={2:['A','B','C'],3:['D','E','F'],4:['G','H','I'],5:['J','K','L'],6:['M','N','O'],7:['P','Q','R','S'],8:['T','U','V'],9:['W','X','Y','Z']}
# def find_key(val):
#     k=(key for key, value in Y.items() if value == val)
#     return k
# X=list(input())
# end=0
# for i in X:
#     th = find_key(i)
#     end+=1+th
# print(end)


# s1=[['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
# qw=list(input())
# total = 0
# for i in qw:
#     for scv in range(8):
#         for w in range(3):
#             if s1[scv][w].find(i) == True:
#                 total+=int(scv)+2
#             else:
#                 pass
# print(total)
qw=list(input())
total=0
for i in qw:
    while True:
        if i == ('A' or 'B' or 'C'):
            total+=3
            break
        elif i == ('D' or 'E' or 'F'):
            total+=4
            break
        elif i == ('G' or 'H' or 'I'):
            total+=5
            break
        elif i == ('J' or 'K' or 'L'):
            total+=6
            break
        elif i == ('M' or 'N' or 'O'):
            total+=7
            break
        elif i == ('P' or 'Q' or 'R' or 'S'):
            total+=8
            break
        elif i == ('T' or 'U' or 'V'):
            total+=9
            break
        else:
            total+=10
            break
print(total)