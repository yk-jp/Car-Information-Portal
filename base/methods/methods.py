from ..config.config import config
import requests
from datetime import date
class RestCarQueryAPI():
    session = requests.Session()
    baseUrl = config.get('externalCarAPI').get('baseUrl')
    Headers = {'User-Agent': 'Mozilla/5.0'}

    def getModels(make=None,model=None,min_year=date.today().year,max_year=date.today().year) -> str:
        url = RestCarQueryAPI.baseUrl + '&cmd=getTrims'
        if(make):
            url += '&make=' + make
        if(model):
            url += '&model=' + model
        if(min_year == None):
            min_year = date.today().year
        url += '&min_year=' + str(min_year)
        if(max_year == None):
            max_year = date.today().year
        url += '&max_year=' + str(max_year)
        return RestCarQueryAPI.session.get(url, headers = RestCarQueryAPI.Headers)

