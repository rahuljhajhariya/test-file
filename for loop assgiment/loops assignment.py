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

# Q13) Write a program to calculate the factorial of a number.

# n=int(input("Enter n: "))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print(f"the factorial of {n} is: {factorial}")

#--------------------------------------------------------------------------------------------------------

# data='rajaram'
# start=0
# end=len(data)-1
# size=len(data)
# while(start<size-1):
#     print(f"start char ={data[start]} ---> end char ={data[end]} ")
#     end-=1
    # if(start==end):
    #     print('--------------------------------',start,end)
    #     start+=1
    #     end=size-1
    # if(data[start]==data[end]):
    #     print('dublicate value',data[start])
    #     start+=1
    #     end=size-1

#-----------------------------------------------------------------------------------------------------------------
# data='14876'
# start=0
# end=len(data)-1
# size=len(data)
# while(start<len(data)-1):
#     # print(int(data[start]),int(data[end]))
#     end-=1
#     if(int(data[start])+int(data[end])==11):
#         print("start =",data[start],"end=",data[end])
    
#     if(start==end):
#         # print('--------------------------------',start,end)
#         start+=1
#         end=size-1
#     if(data[start]==data[end]):
#         # print('dublicate value',data[start])
#         start+=1
#         end=size-1

#----------------------------------------------------------------------------------------------------------------

# Q1. Print 1 to N

# n=int(input("Enter n:" ))
# i=1
# while(i<=n):
#     print(i)
#     i+=1

#----------------------------------------------------------------------------------------------------------------

# Q2. Sum of 1 to N

# n=int(input("Enter n:" ))
# sum=0
# while(n>=1):
#     sum=sum+n
#     n-=1
# print(sum)

#----------------------------------------------------------------------------------------------------------------

# Q3.  Given an integer N, print numbers from N down to 1.

# n=int(input("Enter n:" ))
# while(n>=1):
#     print(n)
#     n-=1

#----------------------------------------------------------------------------------------------------------------

# Q4.  Given an integer N, print all even numbers from 2 to N.

# n=int(input("Enter n: "))

# while(n>=1):
#     if n%2==0:
#         print(n)
#     n-=1

#----------------------------------------------------------------------------------------------------------------

# Q5.  Given N, print all odd numbers from 1 to N.

# n=int(input("Enter n: "))

# while(n>=1):
#     if n%2!=0:
#         print(n)
#     n-=1

#----------------------------------------------------------------------------------------------------------------

# Q6. Given an integer N, print its multiplication table from 1 to 10.

# n=int(input("Enter n: "))
# i=1
# while(i<=10):
#     print(n*i)
#     i+=1

#----------------------------------------------------------------------------------------------------------------

# Q7. Given a string, count the total number of characters without using len().

# n=input("Enter a string: ")
# i=1
# count=0
# while(i<=len(n)):
#     count+=1
#     i+=1
# print(count)

#----------------------------------------------------------------------------------------------------------------

# Q8. Given a positive integer N, find the largest digit in it.

# n= int(input("Enter n: "))
# s=str(n)
# max=0
# i=0

# while(i<len(str(n))):
#     if(int(s[i])>max):
#         max=int(s[i])
#     i+=1
# print("the greatest digit is:",max)

#----------------------------------------------------------------------------------------------------------------

# Q9. Given a string, reverse it using a while loop.

# n=input("Enter a string:")
# length=len(n)-1
# new='' 

# while(length>=0):
#     new=new+n[length]
#     length-=1
# print("new string is:",new)

#----------------------------------------------------------------------------------------------------------------

# Q10. Given a string, count the number of vowels (a, e, i, o, u) using a while loop.

# n=input("Enter a string:")
# count=0
# i=0
# while(i<len(n)):
#     if n[i] in ('a','e','i','o','u'):
#         count+=1
#     i+=1
# print(count)

#----------------------------------------------------------------------------------------------------------------

# Q11. Given an integer N, calculate its factorial using a while loop.

# n=int(input("Enter n: "))
# factorial=1
# while(n>0):
#     factorial=factorial*n
#     n-=1
# print(factorial)

#----------------------------------------------------------------------------------------------------------------

# Q12. Given a positive integer N, count how many digits it has.

# n=int(input("Enter a number: "))
# count=0
# while(n>0):
#     count+=1
#     n//=10
# print("total number of digit are:",count)

#----------------------------------------------------------------------------------------------------------------

# Q13. Given an integer N, reverse its digits.

# n=int(input("Enter a number: "))
# rev=0
# rem=0
# while(n>0):
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# print("reversed number is:",rev)

#----------------------------------------------------------------------------------------------------------------

# Q14. Given an integer N, find the sum of all its digits.

# n=int(input("Enter a number: "))
# sum=0
# rem=0
# while(n>0):
#     rem=n%10
#     sum=sum+rem
#     n//=10
# print("the sum of digits is:",sum)

#----------------------------------------------------------------------------------------------------------------

# Q15. Given an integer N, check if it is a palindrome (reads same forward and backward).

# n=int(input("Enter a number: "))
# temp=n
# rev=0
# rem=0
# while(n>0):
#     rem=n%10
#     rev=rev*10+rem
#     n//=10
# print(rev)
# if(temp==rev):
#     print("number is palindrome")
# else:
#     print("not a palindrome")

#----------------------------------------------------------------------------------------------------------------

# Q16. Given a string, check if it is a palindrome using a while loop.

# n=input("Enter a string: ")
# length=len(n)-1
# new=''
# i=0
# while(length>=0):
#     new=new + n[length]
#     length-=1
# if(n==new):
#     print("string is palindrome")
# else:
#     print("not a palindrome")

#----------------------------------------------------------------------------------------------------------------

# Q17. Given a sentence (string), count the number of words (words are separated by single spaces).

# n=input("Enter a string: ")
# count=1
# i=0
# while(i<len(n)):
#     if(n[i]==' '):
#         count+=1
#     i+=1
# print("number of words in a string is:",count)

#----------------------------------------------------------------------------------------------------------------

# Q18. Given two integers A and B, find their Greatest Common Divisor (GCD).

# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# i=2
# gcd=1
# while(i<=a and i<=b):
#     if(a%i==0 and b%i==0):
#         gcd=gcd*i
#         a//=i
#         b//=i
#         i=1
#     i+=1
# print(gcd)

#----------------------------------------------------------------------------------------------------------------

# Q19. Given a sentence, print each word reversed (words separated by space).

# n=input("Enter a string: ")



#----------------------------------------------------------------------------------------------------------------

# Q20.  Given a string, count the number of consonants (letters that are not vowels a,e,i,o,u)

# n=input("Enter a string: ")
# i=0
# count=0
# while(i<len(n)):
#     if n[i] in ('a','e','i','o','u'):
#         count+=1
#     i+=1
# print(count)

#----------------------------------------------------------------------------------------------------------------

# Q21. Print the first N terms of the Fibonacci series using a while loop.

# n=int(input("Enter n: "))
# a=0
# b=1
# sum=0
# print(a,end=' ')
# print(b,end=' ')
# while(n-2>0):
#     sum=a+b
#     print(sum,end=' ')
#     a=b
#     b=sum
#     n-=1

#----------------------------------------------------------------------------------------------------------------

# Q22. A number is Armstrong if sum of cubes of digits equals the number. Check if N is Armstrong


#----------------------------------------------------------------------------------------------------------------

# Q23. Given an integer N, find all its prime factors.

# n=int(input("enter n: "))

# i=2
# while(i<=n):
#     if(n%i==0):
#         print(i,end=' ')
#         n//=i
#         i=1
#     i+=1

#----------------------------------------------------------------------------------------------------------------

# Q24. A perfect number equals the sum of its proper divisors. Check if N is perfect.

# n=int(input("Enter n: "))
# i=1
# sum=0
# while(i<n):
#     if(n%i==0):
#         sum=sum+i
#     i+=1
# if(sum==n):
#     print("perfect number")
# else:
#     print("not a perfect number")

#----------------------------------------------------------------------------------------------------------------

# Q25. Given a string, count uppercase and lowercase letters separately.

# n=input("Enter a string: ")
# upper=0
# lower=0
# i=0
# while(i<len(n)):
#     if n[i]>='a' and n[i]<='z':
#         lower+=1
#     if n[i]>='A' and n[i]<='Z':
#         upper+=1
#     i+=1
# print(f"lowercase = {lower} and uppercase = {upper}")

#----------------------------------------------------------------------------------------------------------------

# Q26. Given base B and exponent E, compute B^E using only while loop and multiplication.

# b=int(input("enter base: "))
# e=int(input("enter exponent: "))
# power=1
# while(e>0):
#     power=power*b
#     e-=1
# print(power)

#----------------------------------------------------------------------------------------------------------------

# Q27. Given a string, remove duplicate characters and keep only the first occurrence.



#----------------------------------------------------------------------------------------------------------------

# Q28. Given a binary number as a string, convert it to decimal using a while loop.

#----------------------------------------------------------------------------------------------------------------

# Q29. Given N and a string of numbers separated by space (1 to N with one missing), find the missing number

#----------------------------------------------------------------------------------------------------------------

# Q30. Given two strings A and B, check if they are anagrams (same characters, different order).Only use while loops.

#----------------------------------------------------------------------------------------------------------------