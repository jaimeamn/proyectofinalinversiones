
from datetime import datetime
import requests
from flaskapp import COIN_API_URL_BASE, COIN_API_KEY



#{base}/{quota}?time={time}&apikey={apikey}
def getExchange(base, quota):
   print({base, quota})
   date = datetime.now()
   url = COIN_API_URL_BASE + "/" + base + "/" + quota
   headers = {'X-CoinAPI-Key' : COIN_API_KEY}
   response = requests.get(url, headers=headers)
   
   return response.json()



