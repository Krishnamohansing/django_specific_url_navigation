from django.urls import path
from drinks.views import *
app_name='drinks'
urlpatterns = [
    path('Epm/',Epm,name='Epm'),
    path('oldmonk/',oldmonk,name='oldmonk'),
]
