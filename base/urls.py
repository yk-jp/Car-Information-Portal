from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modelList/make/<str:make>',views.modelList,name='modelList')
]