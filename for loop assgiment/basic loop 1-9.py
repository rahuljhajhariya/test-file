#Q1) Write a program to print all natural numbers from 1 to n. – using for loop
# n=int(input("Enter n: "))
# for i in range(1,n+1):
#     print(i)

#------------------------------------------------------------------------------------------------

#Q2) Write a program to print all natural numbers in reverse (from n to 1). –using for loop
# n=int(input("Enter n: "))

# for i in range(n,0,-1):
#     print(i)

#------------------------------------------------------------------------------------------------

#Q3) Write a program to print all alphabets from a to z. – using for loop
# alp='abcdefghijklmnopqrstuvwxyz'
# for i in range(len(alp)):
#     print(alp[i])

#------------------------------------------------------------------------------------------------

#Q4) Write a program to print all even numbers between 1 to 100. – using for loop

# for i in range(1,101):
#     if(i%2==0):
#         print(i,end=' ')

#------------------------------------------------------------------------------------------------

#Q5) Write a program to find the sum of all odd numbers between 1 to n.

# n=int(input("Enter n: "))

# for i in range(1,n+1):
#     if(i%2!=0):
#         print(i,end=' ')

#------------------------------------------------------------------------------------------------

#Q6) Write a program to count the number of digits in a number.
# n=input("Enter n: ")
# count=0
# for i in n:
#     count+=1
# print(f"{count} digit number")

#------------------------------------------------------------------------------------------------

#Q7) Write a program to calculate the sum of digits of a number.

# n=input("Enter n: ")
# sum=0
# for i in n:
#     sum+=int(i)
# print(f"the sum of digits are: {sum}")

#------------------------------------------------------------------------------------------------

#Q8) Write a program to find the first and last digit of a number.

# n=input("Enter n: ")

# print(f"the first digit is: {n[0]}")
# print(f"the last digit is: {n[len(n)-1]}")

#------------------------------------------------------------------------------------------------

#Q9) Write a program to find the sum of first and last digit of a number.

# n=input("Enter n: ")
# sum=0
# first_digit=n[0]
# last_digit=n[len(n)-1]
# sum=int(first_digit)+int(last_digit)
# print(sum)

#------------------------------------------------------------------------------------------------

#Q10) Write a program to enter a number and print its reverse. 

# n=input("Enter n: ")
# for i in range(len(n),0,-1):
#     print(i,end=' ')

#------------------------------------------------------------------------------------------------

#Q11) Write a program to find the power of a number using for loop.

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# power=1
# for i in range(1,b+1):
#     power*=a
# print(f"the power of {a} is: {power}")

#------------------------------------------------------------------------------------------------

#Q12) Write a program to find all factors of a number. 

# n=int(input("Enter n: "))

# for i in range(1,n+1):
#     if(n%i==0):
#         print(i,end=' ')

#------------------------------------------------------------------------------------------------

#Q13) Write a program to calculate the factorial of a number.

# n=int(input("Enter n: "))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(f"the factorial of {n} is: {factorial}")

#------------------------------------------------------------------------------------------------

# n=16
# count=True
# for i in range(2,n):
#     if(n%i==0):
#         count=False
#         break

# if(count==True):
#     print("prime number")
# else:
#     print("not a prime number")

#------------------------------------------------------------------------------------------------

# take n and find the factorial of it

# n=5
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(factorial)

# ------------------------------------------------------------------------------------------------

# take a string and find how many wide sapace are there

# n='re gex  @123'
# count=0
# for i in range(1,len(n)):
#     if(n[i]==" "):
#         count+=1
# print(f"total number of spaces are: {count}")

#------------------------------------------------------------------------------------------------

# take a string and find out the how many numbers are there

# n='regex@1+987423'
# count=0
# for i in range(len(n)):
#     if(n[i]>='0' and n[i]<='9'):
#         count+=1

# print(f"total numbers are: {count}")

#------------------------------------------------------------------------------------------------

#Q) print even number between 1 to 25

# i=1
# while(i<26):
#     if(i%2==0):
#         print(i)
#     i+=1

#------------------------------------------------------------------------------------------------

#Q) 498-306 print the numbers which are divided by 3

# i=306
# while(i<=498):
#     if(i%3==0):
#         print(i)
#     i+=1

#------------------------------------------------------------------------------------------------

#Q) run a loop from a number 2 to the value number 50 and get the sum of all tha natural number

# i=2
# sum=0
# while(i<=50):
#     sum+=i
#     i+=1
# print("the sum of all natural number are: ",sum)

#------------------------------------------------------------------------------------------------

#Q) run a loop from a number 68 to the value number 11 and find how many number are there which are divided by 4

# i=68
# count=0
# while(i>=11):
#     if(i%4==0):
#         count+=1
#     i-=1
# print("number of divisible of 4 between 68 and 11 is: ",count)

#------------------------------------------------------------------------------------------------

#Q) find the prime number

# num=int(input("Enter n: "))
# i=1
# count=0
# while(i<=num):
#     if(num%i==0):
#         count+=1 
#     i+=1
# if(count==2):
#     print("prime number")
# else:
#     print("not a prime number")

#------------------------------------------------------------------------------------------------

#Q) find the factorial of a number

# num=int(input("Enter n: "))
# i=1
# factorial=1
# while(i<=num):
#     factorial=factorial*i
#     i+=1
# print(factorial)

#------------------------------------------------------------------------------------------------

#Q) find the number of digit in a number

# n=465643
# count=0
# while(n>0):
#     count+=1
#     n=n//10
# print(f"the number of digit in a number: ",count)

#------------------------------------------------------------------------------------------------

#Q) find the sum of the digit of a number

# n=1234
# sum=0
# rem=0
# while(n>0):
#     rem=n%10
#     sum=sum+rem
#     n=n//10

# print(f"the sum of the digits of a number is: ",sum)

#------------------------------------------------------------------------------------------------

#Q14)
# n =370
# temp=n
# count=0
# rem=0
# while(n>0):
#     rem=n%10
#     n=n//10
#     count+=1
# n=temp
# total=0
# while(n>0):
#     rem=n%10
#     n=n//10
#     total=total+rem**count
# if(temp==total):
#     print("armstrong number")
# else:
#     print("not")

n=3041
maxi=0
while(n>0):
    rem=n%10
    n=n//10
    if(rem>maxi):
        maxi=rem
print(f"the largest digit in a number is:",maxi)