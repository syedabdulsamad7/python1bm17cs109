def check(s):
    stack=[]
    stack.append('$')
    for i in s:
        if i=='{' or i=='[' or i=='(':
            stack.append(i)
        elif i=='}':
            if stack.pop()=='{':
                pass
            else:
                return False
        elif i==']':
            if stack.pop()=='[':
                pass
            else:
                return False
        elif i==')':
            if stack.pop()=='(':
                pass
            else:
                return False
    if(stack.pop()=='$'):
        return True
    else:
        return False

print(check("}{"))    
        
        
