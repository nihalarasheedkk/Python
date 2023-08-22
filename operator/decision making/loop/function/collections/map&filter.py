#conditn ullath => use filter()  f/n
#no conditn ella sanom print chynel=>map() f/n
#otta output=>reduce()

lst=[1,2,3,4,5]

# squares=list(map(lambda num:num**2,lst))
# print(squares)

# cube=list(map(lambda num:num**3,lst))
# print(cube)

#filter()
#odds
#evens
#num gt>3

# odds=list(filter(lambda num:num%2!=0,lst))
# print(odds)

# evens=list(filter(lambda num:num%2==0,lst))
# print(evens)
                     #single parametr
# gt=list(filter(lambda num:num>3,lst))     #write list comprehnsn method as weell(scrnshot)
# print(gt)

items=[
    {"name":"biriyani","price":130,"category":"nonveg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"},
    
]
#print all item name:
# item_name=list(map(lambda ite:ite.get("price"),items))
# print(item_name)

#lst com=> 
# lst_itemnames=[ite.get("name") for ite in items]
# print(lst_itemnames)

# map_price=list(map(lambda ite:ite.get("price"),items))
# print(map_price)

  #lst c=>
# list_price=[ite.get("price") for ite in items]
# print(list_price)

# filter_veg=list(filter(lambda ite:ite.get("category")=="veg",items))
# print(filter_veg)

list_veg=[ite.get("name") for ite in items if ite.get("category"=="veg") ]
print(list_veg)                   #correctn
#hw watch vid last part