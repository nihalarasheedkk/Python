year=2024
# is_leapyear=False
# if(year%4==0):
#     is_leapyear=True

# elif(year%400==0):
#     is_leapyear=True
# elif(year % 100!=0):
#     is_leapyear=False
#     print(year ,"is leap year",is_leapyear)

if(year%4==0 and year % 400==0 or year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")