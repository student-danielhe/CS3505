import requests
from datetime import datetime

# url to bull current bitcoin price
API_URL = "https://api.coinbase.com/v2/prices/spot?currency=USD" 

# store response
response = requests.get(API_URL)  
responseString = response.text
responseStringList = responseString.split('\"')
# get price from response
price = responseStringList[13]
# get date and time price was pulled
dateAndTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# write date, time, and price to BitcoinDatabase.txt
with open('/home/ec2-user/environment/JakesFolder/BitcoinDatabase.txt', 'a') as f:
    f.write(dateAndTime + " " + price)
    f.write("\n")