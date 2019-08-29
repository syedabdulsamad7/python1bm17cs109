def  func(l1):
     l2=l1
     l1.reverse()
     for i in l1:
          print(i,end=' ')
     l2.reverse()
     print()



     for i in  l2:
          print(i[-1::-1],end=' ')

s=input("enter string")
l3=s.split()
func(l3)        
