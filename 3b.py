import random
for j in range(0,3):
    s=" "
    s=s+chr(random.randrange(97,123))
    s=s+chr(random.randrange(65,91))
    s=s+str(random.randrange(0,10))
    s=s+chr(random.randrange(33,48))
    l=random.randrange(10,16)
    for i in range(4,l):
        c=random.randrange(1,5)
        if(c==1):
           s=s+chr(random.randrange(97,123))
        elif(c==2):
            s=s+chr(random.randrange(65,91))
        elif(c==3):
            s=s+str(random.randrange(0,10))
        else:
            s=s+chr(random.randrange(33,48))
    print(len(s))
    print(s)
    


