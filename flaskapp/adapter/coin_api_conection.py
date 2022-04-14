
from datetime import datetime
from time import time
import requests
import os


#{base}/{quota}?time={time}&apikey={apikey}
def getExchange(base, quota):
    urlBase = os.environ["COIN_API_URL_BASE"]
    fullUrl = str(urlBase + base + "/" + quota + "?" + "time" + "=" + datetime.now + "&" + "apikey" + "=" + os.environ["COIN_API_KEY"])
    rateresponse = requests.get(fullUrl)
    return rateresponse


