from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.today().date()  
    context = {"date":today}
    return render(request, 'foods/index.html', context=context)

    
def food_detail(request, food):  #food paramenter is ~/foods/menu/food < this part
    context = {"name":food}
    return render(request, 'foods/detail.html', context=context)
