num1=8
num2=9
num3=1
if(num1>num2)and(num1>num3):
    if(num2>num3):
        print("second largest number is",num2)
    else:
        print("second largest number is",num3)
elif(num2>num1)and(num2>num3):
    if(num1>num3):
     print("secomd largest number is",num1)
    else:
     print("second largest number is",num3)
elif((num3>num1)and(num3>num2)):
    if(num1>num2):
     print("second largest number is",num1)
else:
    print("second largest number is",num2)