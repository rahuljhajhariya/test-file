# Check whether a year is a leap year

# year=2000

# if(year%4==0 and year%100!=0):
#     print("leap year")
# elif(year%400==0):
#     print("leap year") 
# else:
#     print("not a leap year")
#---------------------------------------------------------------------------------------------------------------------

# year=2024
# if(year%4==0):
#     if(year%100!=0):
#         print("leap year")
#     elif(year%400==0):
#         print("leap year")
#     else:
#         print("not a leap year")
# else:
#     print("not a leap year")

#------------------------------------------------------------------------------------------------------------------------

year=2025
if((year%4==0 and year%100!=0) or year%400==0):
    print("leap year")
else:
    print("not a leap year")