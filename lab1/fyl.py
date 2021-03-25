import random

i=0
mylist=[]
while i<=50:
   num=random.randint(1,200)
   if num % 2==0:
      mylist.append(num)
      i+=1
