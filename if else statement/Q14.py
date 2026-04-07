#Determine BMI category (Underweight / Normal /Overweight / Obese) chain: <18.5, <25, <30, else.

weight=70
height=1.75
bmi=weight/height**2

if(bmi<18.5):
    print("underweight")
elif(bmi<25):
    print("normal")
elif(bmi<30):
    print("overweight")
else:
    print("obse")