import datetime
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from avtosite.forms import Zapis
from .models import *

def index(request):
    posts = Applications.objects.all()
    ttt = Applications.oio
    if request.method == 'POST':
        form = Zapis(request.POST, request.FILES)
        if form.is_valid():
            #print(form.cleaned_data)
            form.save()
            return redirect('/')
    else:
        form = Zapis()


    chas = [{'chas': 10},
            {'chas': 11},
            {'chas': 12},
            {'chas': 13},
            {'chas': 14},
            {'chas': 15},
            {'chas': 15},
            {'chas': 16},
            {'chas': 17},
            {'chas': 18},
            {'chas': 19},
            {'chas': 20},
            {'chas': 21},
            {'chas': 10},
            {'chas': 11},
            {'chas': 12},
            {'chas': 13},
            {'chas': 14},
            {'chas': 15},
            {'chas': 16},
            {'chas': 16},
            {'chas': 17},
            {'chas': 18},
            {'chas': 19},
            {'chas': 20},
            {'chas': 21},
            ]

    nu = [
            {'chas': 1},
            {'chas': 2},
            {'chas': 3},
            {'chas': 4},
            {'chas': 5},
            {'chas': 6},
            {'chas': 7},
            {'chas': 8},
            {'chas': 9},
            {'chas': 10},
            {'chas': 11},
            {'chas': 12},
            {'chas': 13},
            {'chas': 14},
            {'chas': 15},
            {'chas': 16},
            {'chas': 17},
            {'chas': 18},
            {'chas': 19},
            {'chas': 20},
            {'chas': 21},
            {'chas': 22},
            {'chas': 23},
            {'chas': 24},
            {'chas': 25},
            {'chas': 26},
            ]
    now = datetime.datetime.now()
    now1 = now.strftime('%d.%m.%Y')
    tomorrow = now + datetime.timedelta(days=1)
    tim = tomorrow.strftime('%d.%m.%Y')
    NH = now.strftime('%H')
    return render(request, "avtosite/index2.html", {"now": now, "tim": tim, "NH": int(NH), "chas": chas, "now1": now1, 'ttt': posts, 'form': form})


