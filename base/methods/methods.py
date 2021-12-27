from ..config.config import config
import requests


class RestCarQueryAPI():
    session = requests.Session()
    baseUrl = config.get('externalCarAPI').get('baseUrl')
    Headers = {'User-Agent': 'Mozilla/5.0'}

    def getModels(make=None) -> str:
        url = 'https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getModels'
        if(make):
            url += '&make=' + make
        return RestCarQueryAPI.session.get(url, headers = RestCarQueryAPI.Headers)

