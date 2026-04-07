"""
Implement a simple calculator with if-else (no eval)
to perform +, -, *, /. Handle division by zero.
"""

a=5
b=0
opt="/"

if(opt=="+"):
    print(a+b)
elif(opt=="-"):
    print(a-b)
elif(opt=="*"):
    print(a*b)
elif(opt=="/"):
    if(b!=0):
        print(a/b)
    else:
        print("denominator cannot be 0")
