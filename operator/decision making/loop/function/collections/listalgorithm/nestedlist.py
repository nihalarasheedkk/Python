#nested list
#print all nums
lst=[
    [1,2],
    [4,50],
    [50,45]
]
# for sublist in lst:
#     for num in sublist:
#         print(num)

        #short(lst comprehensn) :
# allnumbers=[num for sublist in lst for num in sublist]
# print(allnumbers)

#print all nums >5
# for sublist in lst:
#     for num in sublist:
#         if(num>5):
#             print(num)

# num_gt_five=[num for ls in lst for num in ls if num>5]
# print(num_gt_five)


mobiles=[
    [100,"redminote12",23000,"5g"],
    [101,"oneplusnord",32000,"5g"],
    [102,"iphnoe14",123000,"5g"],
    [103,"s23ultra",133000,"5g"],
    [104,"pexel12",43000,"5g"],
    [105,"nothing",13000,"4g"],
    [106,"galaxya52",23000,"5g"]
        
]
#q1> total number of mobiles
#lst=[2,3,4,5]
# print(len(mobiles),"mobiles available")

#q2> print all mobile names
#for mob in mobiles:
# print(mob[1])
            #value to return is wrote in left
# mobile_names=[mob[1] for mob in mobiles]
# print(mobile_names)

#print 4g mobile's name:
# mobile_nw=[mob[1] for mob in mobiles if mob[3]=="4g"]
# print(mobile_nw)

#print mobile names price <30000:
# mobile_price=[mob[1] for mob in mobiles if mob[2]<30000]
# print(mobile_price)

#print mobile names available in range of 30000 to 50000
# range_filter=[mob[1] for mob in mobiles if mob[2] in range(30000,50001)]
# print(range_filter)

#another way
#range_filter=[mob[1] for mob in mobiles if mob[2]>30000 and mob[2]<50000]
#print(range_filter)

#print all 5g mobile's name under 25000
# price_nw_filter=[mob[1] for mob in mobiles if mob[2]<25000 and mob[3]=="5g"]
# print(price_nw_filter)

items=[
    [1,"potatto",45,"veg",10],
    [2,"tomatto",40,"veg",20],
    [3,"onion",35,"veg",0],
    [4,"brinjal",50,"veg",0],
    [5,"fish",145,"nonveg",10],
    [6,"chicken",145,"nonveg",10],
    [7,"egg",6,"nonveg",100]
 
    
]
"""
total no of products  ~
print 'in stock' product names   
print 'out of stock' "    zero
print veg category product names
product available in range of 50-100
veg products available in range of 40-80
"""
# print(len(items))

#print in stock product names
#last element [-1]
# instock=[item[1] for item in items if item[-1]>0]
# print(instock)

# outofstock=[item[1] for item in items if item[-1]==0]
# print(outofstock)

# veg_product=[item[1] for item in items if item[-2]=="veg"]
# print(veg_product)

# price_filter=[item[1] for item in items if item[2] in range(50,101)]
# print(price_filter)

price_veg=[item[1] for item in items if item[2] in range(40,80) and item[-2]=="veg"]
print(price_veg)

