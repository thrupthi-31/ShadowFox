Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
c=input("Enter a city name:")
if c in Australia:
 print(c,"is in Australia")
elif c in UAE:
 print(c,"is in UAE")
elif c in India:
 print(c,"is in India")
else:
 print("City not found")