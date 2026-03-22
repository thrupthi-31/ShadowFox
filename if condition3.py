Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
c1=input("Enter the first city:")
c2=input("Enter the second city:")
if c1 in Australia and c2 in Australia:
 print("Both cities are in Australia")
elif c1 in UAE and c2 in UAE:
 print("Both cities are in UAE")
elif c1 in India and c2 in India:
 print("Both cities are in India")
else:
 print("They don't belong to the same country")