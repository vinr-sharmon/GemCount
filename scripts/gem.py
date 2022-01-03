print("[INFO] Starting...")
print("[INFO] Updating...")
import requests # make http requests
import json # make sense of what the requests return
import os
import math
gameID = 753

print("[INFO] Update completed")
gemquantity = input("[INPUT] Please input your number of gems >> ")
currency = input("[INPUT] Please input currency \n1 : $, 2 : £, 3 : €, 6 : zł, 8 : ¥, 9 : kr; full list here t.ly/hhTM \n[INPUT] >> ")

print("[INFO] Requesting price data from Steam market...")
URL = "https://steamcommunity.com/market/priceoverview/?appid=753&currency=" + currency + "&market_hash_name=753-Sack%20of%20Gems"
r = requests.get(url = URL)
data = r.json()
print("[WARN] If there is an error or nothing happens Steam is rate limiting you, try again  in a few minutes")
print("[INFO] Steam returned data succesfully: " + str(data['success']) + " >> " + data['lowest_price'])

print("[INFO] Calculating...")
s = data['lowest_price'].replace(",",".")
newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in s)
price = [float(i) for i in newstr.split()]

pricefloat = price[0]
priceonegem = pricefloat / 1000
priceallgems = priceonegem * float(gemquantity)
priceallgemsfee = priceallgems / 1.05
priceallgemsround = round(priceallgems, 2)
priceallgemsfeeround = round(priceallgemsfee, 2)


print("[INFO] Calculations complete")
print("\n[ROUNDED] You have " + str(priceallgemsround).replace(".",",") + "[currency] in gems before Steam fees and " + str(priceallgemsfeeround).replace(".",",") + "[currency] after them.")

print("\n[NOT ROUNDED] You have " + str(priceallgems).replace(".",",") + "[currency] in gems before Steam fees and " + str(priceallgemsfee).replace(".",",") + "[currency] after them.")

os.system("pause")