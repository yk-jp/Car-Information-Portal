from ..config.config import config
import requests
from datetime import date
class RestCarQueryAPI():
    session = requests.Session()
    baseUrl = config.get('externalCarAPI').get('baseUrl')
    Headers = {'User-Agent': 'Mozilla/5.0'}

    def getModels(make=None,min_year=date.today().year,max_year=date.today().year) -> str:
        url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&model'
        if(make):
            url += '&make=' + make
        url += '&{min_year}&{max_year}'
        return RestCarQueryAPI.session.get(url, headers = RestCarQueryAPI.Headers)

    

