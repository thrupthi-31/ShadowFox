def format_example(a,b):
    return"First value:{},Second value:{}".format(a,b)
print(format_example(145,'o'))
pi=3.14
r=84
area=pi*r*r
print("Area of pond:",area)
water_per_sq_m=1.4
total_water=area*water_per_sq_m
print("Total water in pond:",int(total_water))
distance=490
time_minutes=7
time_seconds=time_minutes*60
speed=distance/time_seconds
print("Speed in meters per second:",int(speed))