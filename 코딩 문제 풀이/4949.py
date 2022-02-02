#균형잡힌 괄호
while True:
    x=input()
    stack = []
    for i in x:
        if i == ".":
            break
        else:
            if i=="(" or i=="[":
                stack.append(i)
            else:
                if i==")":
                    if len(stack) !=0 and stack[-1] =="(":
                        stack.pop()
                    else:
                        stack.append(i)
                elif i == "]":
                    if len(stack) != 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append(i)
    if len(stack) ==0:
        print("yes")
    else:
        print("No")



