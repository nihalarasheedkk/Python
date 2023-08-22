tummy_size=0.5
buttock_size=0.5

healthrisk=tummy_size/buttock_size
print(healthrisk)
gender1="male"
gender2="female"

if(gender2):
    print("male")
    if(healthrisk<=0.80):
        print("low")
    else:
        (0.81>healthrisk<=0.85)
        print("moderate")
    if(healthrisk>0.85):
        print("high")

elif(gender1):
    print("female")
    if(healthrisk<=0.95):
            print("low")
    else:
         (0.96>healthrisk<=1.0)
         print("moderate")
         if(healthrisk>1.0):
              print("high")
         
    

