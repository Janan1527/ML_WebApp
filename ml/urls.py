from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mlapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index,name='Homepage'),
    url('PredictSpecies',views.PredictSpecies,name='PredictSpecies'),
    url('viewDatabase',views.viewDatabase,name='viewDatabase'),
    url('updateDataBase',views.updateDataBase,name='updateDataBase'),
]
