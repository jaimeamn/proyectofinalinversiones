
from datetime import datetime
import requests
from flaskapp import COIN_API_URL_BASE, COIN_API_KEY



#{base}/{quota}?time={time}&apikey={apikey}
def getExchange(base, quota):
   date = datetime.now()
   print(COIN_API_URL_BASE.format(base, quota,date,COIN_API_KEY))
   rateResponse = requests.get(COIN_API_URL_BASE.format({base, quota,date,COIN_API_KEY}))
   return rateResponse


