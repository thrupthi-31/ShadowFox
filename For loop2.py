total=0
for i in range(10,101,10):
 print("Do 10 jumping jacks")
 total+=10
 a=input("Are you tired? ")
 if a=="yes" or a=="y":
  b=input("Do you want to skip remaining sets? ")
  if b=="yes" or b=="y":
   print("You completed a total of",total,"jumping jacks")
   break
 else:
  if total<100:
   print(100-total,"jumping jacks remaining")
if total==100:
 print("Congratulations! You completed the workout")