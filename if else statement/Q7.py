# Determine the type of a triangle given three sides

a=3
b=4
c=5

if(a+b>c and a+c>b and b+c>a):
    if(a==b and a==c and b==c):
        print("the triangle is equilateral")
    elif(a==b or a==c):
        print("the triangle is isosceles")
    else:
        print("the triangle is scalene")
else:
    print("it is not a valid triangle")

