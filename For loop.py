import random
c6=0
c1=0
t=0
p=0
for i in range(20):
 r=random.randint(1,6)
 if r==6:
  c6+=1
 if r==1:
  c1+=1
 if r==6 and p==6:
  t+=1
 p=r
print("6 rolled:",c6)
print("1 rolled:",c1)
print("two 6s in a row:",t)