class CallDetail:
    c1=0
    c2=0
    c3=0
    def __init__(self,c,r,d,co):
         self.c1=c
         self.rcv=r
         self.dur=d
         self.code=co
    def disp(self):
         print(self.c1,self.rcv,self.dur,self.code)
         
              

class util:
     def __init__(self):
         self.list_of_call_objects=[]
     def parse_customer(self,list_of_call_string):
          for i in list_of_call_string:
               x=i.split(",")
               o=CallDetail(*x)
               self.list_of_call_objects.append(o)
     def display(self):
          for i in self.list_of_call_objects:
               i.disp()
call1='1234,4321,10,STD'
call2='5678,8765,20,Local'
call3='9632,2369,30,ISD'

list_of_call_string=[call1,call2,call3]
util().parse_customer(list_of_call_string)
ob=util()
ob.parse_customer(list_of_call_string)
ob.display()
