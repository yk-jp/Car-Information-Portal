from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modelList/<str:make>',views.modelList,name='modelList'),
    path('modelList/<str:make>/<str:model>',views.modelDetails,name='modelDetails')
]