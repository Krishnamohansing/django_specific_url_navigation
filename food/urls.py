from django.urls import path
from food.views import *
app_name='food'
urlpatterns = [
    path('biryani/',biryani,name='biryani'),
    path('dbc/',dbc,name='dbc'),
]
