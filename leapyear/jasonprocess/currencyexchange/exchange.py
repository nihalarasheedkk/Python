rates={  
    "USD": 1,
    "AED": 3.6725,
    "AFN": 86.0330,
    "ALL": 97.5499,
    "AMD": 386.9256,
    "ANG": 1.7900,
    "AOA": 824.0658,
    "ARS": 254.7465,
    "AUD": 1.5099,
    "AWG": 1.7900,
    "AZN": 1.6979,
    "BAM": 1.7974
    }
#currency exchange rate application

#currency exchange

amount=int(input("enter amount >"))#2
from_cur_code=input("enter currency code >")#usd
to_cur_code=input("enter destination currency code :>")#inr

# from json import load
# with open("C:\Users\user\OneDrive\Desktop\mypythonprograms\leapyear\jasonprocess\currencyexchange\db.json")as f:
#     data=load(f)

# rates=data.get("conversion_rates")
# amount=int(input("enter amount >"))
# fromcurrencycode=input("enter destination currency code :>")

from_rate=rates.get(from_cur_code)
to_rate=rates.get(to_cur_code)

result=(amount/from_rate)*to_rate
print(result)

# result=(amount/from_code_rate)*to_currency_code_rate
# print(result)
# # to_rate