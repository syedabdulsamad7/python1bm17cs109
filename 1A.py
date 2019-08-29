lst=[]
n=int(input("enter number of elements :"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)

lst2=[]
for i in range(0,n):
    if lst[i]%2==0:
        lst2.append(lst[i])
    
print(lst2)    
