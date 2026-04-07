"""
Income tax calculator with slabs using nested if-else

Hint: Use nested if-else to first check income range then apply progressive tax rates per slab.
| Income Range  | Tax Rate |
| ------------- | -------- |
| 0 - 2.5 lakh  | 0%       |
| 2.5 - 5 lakh  | 5%       |
| 5 - 10 lakh   | 20%      |
| Above 10 lakh | 30%      |

"""

income=int(input("Enter your income: "))
tax=0
if income>0:
    if income>1000000:
        tax=(income-1000000)*0.3
        income=income-1000000
    if income>500000 and income<=1000000:
        tax=tax+(income-500000)*0.2
    if income>250000 and income<=500000:
        tax=tax+(income-250000)*0.05
else:
    print("enter the correct amount: ")
print(f"the tax is: {tax}")    