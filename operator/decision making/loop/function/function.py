# #function r usd to perform a specific task
# #print(): to display msg in console (staic)
# #input(): to read ms frm console
# # num1=input("enter the number:")
# # print(num1)              #some f/n return value like type,input
# """
# def function_name(parameters)
# function definition
# return value
# """

# # def add(num1,num2):
# #  res=num1+num2
# #  return res   #araeya return
# # print(add(30,10))

# #create a function multiplication with three parameter
# # def mul(n1,n2,n3):
# #     res=n1*n2*n3
# #     return res
# # print(mul(2,2,2))

# # def max_two(n1,n2):
# #     if(n1>n2):
# #         return n1
# #     else:
# #         return n2
# # print(max_two(2,8))


# #cut shortin
# # def max_two(n1,n2):
# #     return n1 if n1>n2 else n2
# # print(max_two(2,8))

# # def min_two(n1,n2):
# #     return n1 if n1<n2 else n2
# # print(min_two(2,4))                  #hw hollow pyramid,create a function max_three (3 parameters) max of num

# def max_three(n1,n2,n3):
# #     if(n1>n2) and (n1>n3):
# #         return n1
# #     if(n2>n1) and (n2>n3):
# #         return n2
# #     else:
# #         return n3
# # print(max_three(11,2,5))

# #short
# #  return n1 if (n1>n2) and (n1>n3) else n2 if n2>n3 else n3
# # print(max_three(2,5,8))

# #  def smart_sub(n1,n2):

# #     return n1-n2 if n1>n2 else n2-n1          #didnt get
# #  print(smart_sub(40,50))

# def factorial(num):
#     fact=1
#     for i in range(1,(num+1)):
#         fact*=i
#     return fact
# print(factorial(4))

# def is_prime(num):
#     is_prime=True
#     for i in range(2,num):
#         if(num%i==0):
#             is_prime=False
#             break
#         return "prime numb" if is_prime==True else "not prime"
# print(is_prime(27))

# for row in range(1,5):
#     for column in range(1,8):
#         if(row==4)or(row+column==5)or(column-row==3):
#             print("*", end="")
#         else:
#             print(end=" ")            #gpt yt
#     print()  #nxt line

# for row in range(1,5):
#     for column in range(1,8):
#         if(row==1)or(row==column)or(row+column==8):
#             print("*",end="")  #
#         else:
#             print(end=" ")
#     print()

#hw full pyramid
for row in range(1,5):
    for column in range(1,8):
            if(row==4,-3):
              print("*",end="")
            print(end=" ")
    print()
