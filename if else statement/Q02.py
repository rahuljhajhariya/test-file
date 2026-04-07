"""
Write a program that takes an integer input from the user and prints the corresponding day of the week.
The days follow this pattern:
1 → Sunday
2 → Monday
3 → Tuesday
4 → Wednesday
5 → Thursday
6 → Friday
7 → Saturday
"""

day=15
day=day%7
if(day==1):
    print("sunday")
elif(day==2):
    print("monday")
elif(day==3):
    print("tuesday")
elif(day==4):
    print("wednesday")
elif(day==5):
    print("thrusday")
elif(day==6):
    print("friday")
else:
    print("saturday")