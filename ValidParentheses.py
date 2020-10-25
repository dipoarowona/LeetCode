def isValid(s):

    stack = []
    
    for i in s:
        if i =="[" or i =="{" or i =="(":
            stack.append(i)
        else:
            if len(stack)>0 and i=="]" and stack[-1]=="[":
                stack.pop(-1)
            elif len(stack)>0 and i=="}" and stack[-1]=="{":
                stack.pop(-1)
            elif len(stack)>0 and i==")" and stack[-1]=="(":
                stack.pop(-1)  
            else:
                return False
    
    return len(stack)==0


s="{}{}{}({[]})"
print(isValid(s))