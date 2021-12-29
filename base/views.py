from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.urls import reverse
import requests
import json
# importing date class from datetime module
from datetime import date
# custom modules
from .config.config import config
from .methods.methods import RestCarQueryAPI
from .methods.convertToModelDetails import convertToModelDetails

todays_date = date.today() #today's date

# Create your views here.
def index(request):
    carMakers = config.get('GermanCarMaker') 
    context = {
        'carMakers':carMakers,
        'years':range(1886,todays_date.year + 1)
    }    
    if request.method =='POST':
        # post data
        make = request.POST.get('carMake') if request.POST.get('carMake') != '' else None
        model = request.POST.get('carModel') if request.POST.get('carModel') != '' and request.POST.get('carModel') != 'CAR MODEL' else None
        beginYear = request.POST.get('beginYear') if request.POST.get('beginYear') != '' else None
        endYear = request.POST.get('endYear') if request.POST.get('endYear') != '' else None

        img = carMakers[make] if make else None
        req = RestCarQueryAPI.getModels(make,model,beginYear,endYear)
        modelDetailsData = json.loads(req.text[2:-2]).get('Trims')
        modelDetails = convertToModelDetails(modelDetailsData)

        modelDetailTitles = ['model_year','model_name','model_engine_power_ps']
        context = {
        'carMakers':carMakers,
        'modelDetailTitles':modelDetailTitles,
        'modelDetails':modelDetails,
        'img':img,
        'years':range(1886,todays_date.year + 1)
        }
        return render(request,'pages/modelDetails.html',context)

    return render(request,'pages/index.html',context)

def modelList(request,make=None):
    carMakers = config.get('GermanCarMaker') 
    img = carMakers[make]

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

def modelDetails(request,make,model):
    carMakers = config.get('GermanCarMaker') 
    img = carMakers[make]
    req = RestCarQueryAPI.getModels(make,model)
    modelDetailsData = json.loads(req.text[2:-2]).get('Trims')
    modelDetailTitles = ['model_year','model_name','model_engine_power_ps']
    modelDetails = convertToModelDetails(modelDetailsData)

    context = {
       'carMakers':carMakers,
       'modelDetailTitles':modelDetailTitles,
       'modelDetails':modelDetails,
       'img':img,
       'years':range(1886,todays_date.year + 1)
    }
    return render(request,'pages/modelDetails.html',context)