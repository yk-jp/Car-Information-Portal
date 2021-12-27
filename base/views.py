from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# custom modules
from .config.config import config
from .methods.methods import RestCarQueryAPI


# Create your views here.
def index(request):

    carNakers = config.get('GermanCarMaker') 
    # req = RestCarQueryAPI.getModels()

    # print(req.status_code)

    return render(request,'pages/index.html',{'carMakers':carNakers})

def modelList(request,make):
    carNakers = config.get('GermanCarMaker') 
    if request.method == 'GET':
        req = RestCarQueryAPI.getModels(make)
        models = json.loads(req.text[2:-2]).get('Models')
        print(models)
        return render(request,'pages/modelList.html',{'carMakers':carNakers ,'make':make,'models':models})

    return render(request,'pages/modelList.html',{'carMakers':carNakers})