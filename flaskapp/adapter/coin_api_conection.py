
from datetime import datetime
from locale import currency
from time import time
import requests
import os
from flaskapp import COIN_API_URL_BASE, COIN_API_KEY
from flaskapp.main import getExchangeType


#{base}/{quota}?time={time}&apikey={apikey}
def getExchange(base, quota):
    base = getExchangeType

    date = datetime.now()
    requests.get(COIN_API_URL_BASE.format( base, quota, 

    ))
    
    rateresponse = requests.get(fullUrl)
    return rateresponse


