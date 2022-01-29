#벌집피자
x = int(input())
spin =1
cou=0
y=1
sample=0
while True:
    cou+=1
    for y in range(spin+1):
        if y == x:
            sample=x
            break
        else:
            continue
    y=spin+1
    spin = spin + (6 * cou)
    if sample==x:
        print(cou)
        break



