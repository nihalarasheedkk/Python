from json import load

with open("C:\\Users\\user\\OneDrive\\Desktop\\mypythonprograms\\leapyear\\jasonprocess\\currencyexchange\\restcountries\\rest.json",encoding="UTF-8") as f:
    data=load(f)

# print(len(data))

# print all country name

all_countries_name=[c.get("name") for c in data]
# print(all_countries_name)

#print all region name

region_name={c.get("region") for c in data}   #gave set cuz duplications wont be occur
# print(region_name)  

asian_countries=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_countries)

#print population of afghanistan
population_afghanistan=[c.get("population") for c in data if c.get("name")=="Afghanistan"]
# print(population_afghanistan)     

#indian borders sharing

# country_borders=[c.get("borders") for c in data if c.get("name")=="India"][0]

# country_borders_name=[c.get("name") for c in data if c.get("alpha3Code") in country_borders]
# print(country_borders_name)

#currency
currency_code=[c.get("name") for c in data if c.get("code")=="IND"]
print(currency_code)

#countey with highet pop