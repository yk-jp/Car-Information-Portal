import os

CarMaker = ['audi', 'bmw', 'mercedes', 'porsche', 'volkswagen']

GermanCarMaker = {
    'audi': os.path.join('img', 'carMaker_logo', 'audi.jpg'),
    'bmw':  os.path.join('img', 'carMaker_logo', 'bmw.jpg'),
    'mercedes': os.path.join('img', 'carMaker_logo', 'mercedes.jpg'),
    'porsche': os.path.join('img', 'carMaker_logo', 'porsche.jpg'),
    'volkswagen': os.path.join('img', 'carMaker_logo', 'volkswagen.jpg')
}

externalCarAPI ={
  'baseUrl':'https://www.carqueryapi.com/api/0.3/?callback=?'
} 

config = {
  'GermanCarMaker': GermanCarMaker,
  'externalCarAPI':externalCarAPI
}