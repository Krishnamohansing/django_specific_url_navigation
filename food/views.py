from django.shortcuts import render

# Create your views here.
def biryani(request):
    return render(request,'biryani.html')
def dbc(request):
    return render(request,'dbc.html')