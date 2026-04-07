"""
Determine day type and shift from hour and weekday flag
classifies hour into Morning / Afternoon / Evening / Night.
"""

day= input("Enter the day: ")
time=int(input("Enter the shift time: "))

#here we find working days
if day in ("monday","tuesday","wednesday","thrusday"):
    if time>=0 and time<=6:
        print("morning shift, weekday")
    elif time>6 and time<=12:
        print("afternoon shift, weekday")    
    elif time>12 and time<=18:
        print("evening shift, weekday")
    elif time>18 and time<=24:
        print("night shift, weekday")

#here we find weekend days
elif day in ("saturday","sunday"):
    if time>=0 and time<=6:
        print("morning shift, weekend")
    elif time>6 and time<=12:
        print("afternoon shift, weekend")    
    elif time>12 and time<=18:
        print("evening shift, weekend")
    elif time>18 and time<=24:
        print("night shift, weekend")
else:
    print("Enter correct date and time")