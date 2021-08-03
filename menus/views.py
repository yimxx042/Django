from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.today().date()
    context = {"today":today}
    return render(request, 'menus/index.html', context)


def detail(request, menu):
    return render(request, 'menus/detail.html')