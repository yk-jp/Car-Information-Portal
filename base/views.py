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

    context = {
        'carMakers':carNakers,
        'years':range(1886,todays_date.year + 1)
    }
    return render(request,'pages/index.html',context)

def modelList(request,make):
    carMakers = config.get('GermanCarMaker') 
    img = carMakers[make]

    if request.method == 'GET':
        req = RestCarQueryAPI.getModels(make)
        modelsData = json.loads(req.text[2:-2]).get('Trims')

        models = []

        for model in modelsData:
            if model['model_name'] not in models: models.append(model['model_name'])

        context = {
            'carMakers':carMakers,
            'make':make,
            'models':models,
            'img':img,
            'years':range(1886,todays_date.year + 1)
        }
        return render(request,'pages/modelList.html',context)
    
    # elif request.method =='POST':
    #     print('')

    return render(request,'pages/modelList.html',{'carMakers':carMakers})