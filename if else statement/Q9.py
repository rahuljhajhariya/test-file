"""
Find the roots of a quadratic equation using if-else
D = b^2 - 4ac. Use nested if-else for D&gt;0 (two roots), D=0 (one root), D&lt;0 (no real roots).
"""

a=1
b=3
c=8
d=b**2-4*a*c

if(d>0):
    print("two roots")
elif(d<0):
    print("no real roots")
else:
    print("one root")