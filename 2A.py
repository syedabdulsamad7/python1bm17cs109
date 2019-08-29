def fun(lst,n):
    flag=0
    for i in lst:
        if i==n:
           flag=1
           break;

    if flag==1:
         return True
    else:
         return False


lst=[]
x=int(input("enter the size of list"))
for j in range(0,x):
    ele=int(input())
    lst.append(ele)

n=int(input("enter the key"))
print(fun(lst,n))
    
