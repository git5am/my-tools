import requests
import json
import time
import datetime

# defining vitex api
url = "https://vitex.vite.net/api/v1/exchange-rate?tokenSymbols=VITC-000"
# connecting to the api
response = requests.get(url)
# printing success
print("Connection To ViteX API Successful!")

# setting up parsing
response = requests.get(url)
data = response.text
parsed = json.loads(data)
data = parsed["data"]
type(data)
usdRate = data[0]['usdRate']
i = 0

time.sleep(1)
# printing VITC value!
while i <= 10:
    print("VITC's value in dollars is " + str(usdRate))
    localtime = time.asctime( time.localtime(time.time()) )
    print("===Local current time :" + localtime + "===")
    time.sleep(0.5)
