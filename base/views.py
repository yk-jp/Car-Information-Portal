from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
import requests
import json
# importing date class from datetime module
from datetime import date
# custom modules
from .config.config import config
from .methods.methods import RestCarQueryAPI

todays_date = date.today() #today's date


# Create your views here.
def index(request):

    carNakers = config.get('GermanCarMaker') 
    # req = RestCarQueryAPI.getModels()

    # print(req.status_code)
    context = {
        'carMakers':carNakers,
        'years':range(1886,todays_date.year + 1)
    }
    return render(request,'pages/index.html',context)

def modelList(request,make):
    carNakers = config.get('GermanCarMaker') 
    if request.method == 'GET':
        req = RestCarQueryAPI.getModels(make)
        models = json.loads(req.text[2:-2]).get('Models')
        context = {
            'carMakers':carNakers,
            'make':make,
            'models':models
        }
        return render(request,'pages/modelList.html',context)

    return render(request,'pages/modelList.html',{'carMakers':carNakers})