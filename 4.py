class univauto:
         def __init__(self,sid,age, marks):
             self.__sid=None
             self.__age=None
             self.__marks=None
         def validate_marks(self):
            if(self.marks>=0 and self.marks<=100):
                return True
            else:
                 return False
         def validate_age(self):
             if(self.age>20):
                  return True
             else:
                   return False
         def check_qualification(self):
             if(self.marks>=65 and self.age>20):
                    return True
             else:
                     return False
         def settler(self):
             self.sid=int(input("enter student id"))
             self.age=int(input("enter age"))
             self.marks=int(input("enter marks"))
         def getter(self):
             print("marks",self.validate_marks())
             print("age",self.validate_age())
             print("qualification",self.check_qualification())


ob=univauto()
ob.settler()
ob.getter()


