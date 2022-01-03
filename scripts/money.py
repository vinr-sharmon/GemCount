print("[INFO] Starting...")
print("[INFO] Updating...")
import requests # make http requests
import json # make sense of what the requests return
import os
import math
gameID = 753

print("[INFO] Update completed")
bank = input("[INPUT] Please input  the ammount of money you want to spend(without currency, with . not ,) >> ")
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
times = float(bank) / price[0]
timesround = math.trunc(times)

print("[INFO] Calculations complete")

print("\nYou can buy " + str(timesround).replace(".0", "") + "000 gems.")

os.system("pause")