"""
Q19 Validate a date (day, month, year) using nested if-else
Hint: Check year &gt; 0, then month 1-12, then days-per-month (accounting for leap years with nested if-else).
"""
day=int(input("enter the day: "))
month=int(input("enter the month number : "))
year=int(input("enter the year: "))

if year>0:
    #date check for 31 
    if month in (1,3,5,7,8,10,12):
        if day>=1 and day<=31:
            print("valid date")
        else:
            ("invalid date")
    elif month in (4,6,9,11):
        if day>=1 and day<=30:
            print("valid date")
        else:
            print("invalid date")
    elif month==2:
        if(year%4==0 and year%100!=0) or year%400==0:
            if day>=1 and day<=29:
                print("valid date")
            else:
                print("invalid date")
        else:
            if day>=1 and day<=28:
                print("valid date")
            else:
                print("invalid year")
    else:
        print("invalid year")
else:
    print("invalid year")
