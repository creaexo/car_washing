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
    send_mes = 0



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

    now = datetime.datetime.now()
    now1 = now.strftime('%d.%m.%Y')
    tomorrow = now + datetime.timedelta(days=1)
    tim = tomorrow.strftime('%d.%m.%Y')
    NH = now.strftime('%H')

    if request.method == 'POST':
        form = Zapis(request.POST, request.FILES)
        if form.is_valid():
            send_mes = 1
            form.save()
            form = Zapis()
            return render(request, "avtosite/index2.html", {"now": now, "tim": tim, "NH": int(NH), "chas": chas, "now1": now1, 'ttt': posts, 'form': form, 'send_mes': send_mes})
    else:
        form = Zapis()
    if len(form.errors) != 0:
        send_mes = 2
    return render(request, "avtosite/index2.html", {"now": now, "tim": tim, "NH": int(NH), "chas": chas, "now1": now1, 'ttt': posts, 'form': form, 'send_mes': send_mes})


