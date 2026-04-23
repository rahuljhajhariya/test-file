data='regex software'
newst=''
# for i in range(len(data)):
#     if(data[i] not in ('a','e','i','o','u')):
#         newst=newst+data[i]
    
# print(f"new string = {newst}")




# for i in range(len(data)):
#     if(data[i]=='a' or data[i]=='e' or data[i]=='i' or data[i]=='o' or data[i]=='u'):
#         continue
#     else:
#         newst=newst+data[i]
    
# print(f"new string = {newst}")


# sentence="i love india"
# result = ''
# word = ''
# i = 0
# j=0
# while i <= len(sentence):
#     if i == len(sentence) or sentence[i] == ' ':
#         rev = ''
#         j = len(word) - 1
#         while j >= 0:
#             rev += word[j]
#             j -= 1
#         result += rev + (' ' if i < len(sentence) else '')
#         word = ''
#     else:
#         word += sentence[i]
#         i += 1
# print(result)

#---------------------------------------------------------------------------------------------------------------

# Q 2-100 prime number

# i=2

# while(i<=100):
#     j=2
#     count=0
#     while(j<=i):
#         if (i%j==0):
#             count+=1
#         j+=1
#     if(count==1):
#         print(i,end=" ")
#     i+=1

#---------------------------------------------------------------------------------------------------------------

# Q 2-400 non prime number

# i=2

# while(i<=400):
#     j=2
#     count=0
#     while(j<=i):
#         if (i%j==0):
#             count+=1
#         j+=1
#     if(count>1):
#         print(i,end=" ")
#     i+=1

#---------------------------------------------------------------------------------------------------------------.

# Q 100-600 strong number

# i=100

# while(i<=600):
#     temp=i
#     sum=0
#     while(temp>0):
#         factorial=1
#         rem=temp%10
#         temp//=10    
#         while(rem>0):
#             factorial=rem*factorial
#             rem-=1
#             # print(factorial)
#         sum=sum+factorial
#     if(sum==i):
#         print("strong number=",i)
#     i+=1

