"""
Determine if a point lies inside, on, or outside a circle
"""
cx=0
cy=0
r=5
px=3
py=4
d=1
d**2 == (cx-px)**2 +(cy-py)**2

if(d**2>r**2):
    print("outside the circle")
elif(d**2<r**2):
    print("inside the circle")
else:
    print("on the circle")