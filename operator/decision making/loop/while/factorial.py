# # #print factorial of a number 5*4*3*2*1
# num=5                   #give any
# fact=1                  #since multiplication
# while(num>=1):           #condition
#     fact*=num                #  *= -=  +=
#     num-=1                   #decrement
#     print(fact)               #print("factorial",fact)


#print all even numbers within a range
# num=1
# while(num<=10):
#     if(num%2==0):
#         print(num)
#     num+=1

# num=1
# while(num<=20):
#     if(num%2!=0):
#         print(num)
#     num+=1

#if given 2(24 should be print)        if 3  369  (2+22)   (3+33=333) (4+44+444+4444)    HW
#sum of all even and odd numbers=>   HW

# num=1
# while(num<=10):
#     if(num%2==0):
#         print(num)
#         num+=1
   

n=1
sum_even=0
sum_odd=0
while(n<=10):
    if(n%2==0):
     sum_even+=n
    else:
       sum_odd+=n
n+=1

