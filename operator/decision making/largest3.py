num1=10
num2=20
num3=30
# if((num1>num2) and (num1>num3) ):
#     print(" num1 is large")
# elif((num2>num1) and (num2>num3)):
#     print("num2 is large")
# elif((num3>num1) and (num3>num2)):
#     print("num3 is large")

    
# second largest number hw
#sort these three numbers   ascending or descending
#calculate bmi(body mass index) weight in kg height=cm = meter
#BMI=weight/height in meter **

#sort
# if(num1>num2>num3):
#     print(num1,num2,num3)
# elif(num2>num3>num1):
#     print(num2,num3,num1)
# elif(num3>num2>num1):
#     print(num3,num2,num1)

if(num1>num2) and (num1>num3):
    if(num2>num3):
        print(num2,"is second largest")
    else:
        print(num3, "is second largest")
elif(num2>num1) and (num2>num3):
    if(num1>num3):
        print(num1, "is second largest")
    else:
        print(num3,  "second largest")
elif(num3>num1) and (num3>num2):
    if(num1>num2):
        print(num1, "is second largest")
    else:
        print(num2, "is second largest number")


