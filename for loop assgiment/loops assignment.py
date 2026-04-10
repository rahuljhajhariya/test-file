#Q1) Write a program to print all natural numbers from 1 to n. – using while loop

# n=int(input("Enter n: "))
# i=1
# while(i<=n):
#     print(i,end=" ")
#     i+=1

#------------------------------------------------------------------------------------------------

#Q2) Write a program to print all natural numbers in reverse (from n to 1). –using while loop

# n=int(input("Enter n: "))
# while(n>=1):
#     print(n,end=" ")
#     n-=1

#------------------------------------------------------------------------------------------------

#Q3) Write a program to print all alphabets from a to z. – using while loop



#------------------------------------------------------------------------------------------------

#Q4) Write a program to print all even numbers between 1 to 100. – using while loop

# n=100
# while(n>=1):
#     if(n%2==0):
#         print(n,end=" ")
#     n-=1

#------------------------------------------------------------------------------------------------

#Q5) Write a program to find the sum of all odd numbers between 1 to n.

# n=int(input("Enter n: "))
# sum=0
# while(n>=1):
#     if(n%2!=0):
#         sum=sum+n
#     n-=1
# print(sum)

#------------------------------------------------------------------------------------------------

#Q6) Write a program to count the number of digits in a number.

# n=int(input("Enter n: "))
# count=0
# while(n>0):
#     count+=1
#     n=n//10
# print(f"number of digits are:",count)

#------------------------------------------------------------------------------------------------

#Q7) Write a program to calculate the sum of digits of a number.

# n=int(input("Enter n: "))
# sum=0
# rem=0
# while(n>0):
#     rem=n%10
#     sum=sum+rem
#     n=n//10
# print(f"sum of all digits of a number is:",sum)

#------------------------------------------------------------------------------------------------

#Q8) Write a program to find the first and last digit of a number.

# n=int(input("Enter n: "))
# a=len(str(n))
# multiple=1
# while(a>1):
#     multiple=multiple*10
#     a-=1
# print(f"first digit is:",n//multiple)
# print(F"last digit is:",n%10)

#------------------------------------------------------------------------------------------------

#Q9) Write a program to find the sum of first and last digit of a number.

# n=int(input("Enter n: "))
# a=len(str(n))
# sum=0
# multiple=1
# while(a>1):
#     multiple=multiple*10
#     a-=1
# print(f"the sum of first and last digit is:",n//multiple+n%10)

#------------------------------------------------------------------------------------------------

#Q10) Write a program to enter a number and print its reverse. 

# n=int(input("Enter n:"))
# rev=0
# rem=0
# while(n>0):
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(f"the reversed number is:",rev)

#------------------------------------------------------------------------------------------------

#Q11) Write a program to find the power of a number using for loop.

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# power=1
# while(b>0):
#     power=power*a
#     b-=1
# print(f"the power of {a} is:",power)

#------------------------------------------------------------------------------------------------

#Q12) Write a program to find all factors of a number. 

# n=int(input("Enter n: "))
# i=1
# while(i<=n):
#     if(n%i==0):
#         print(i,end=" ")
#     i+=1

#------------------------------------------------------------------------------------------------

#Q13) Write a program to calculate the factorial of a number.

# n=int(input("Enter n: "))
# factorial=1
# while(n>=1):
#     factorial=factorial*n
#     n-=1
# print(f"the factorial is:",factorial)

#------------------------------------------------------------------------------------------------

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

# n=int(input("Enter n: "))
# count=0
# for i in range(1,len(str(n))+1):
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