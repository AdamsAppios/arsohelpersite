from django.http import JsonResponse
from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect
from django.template import loader
from .models import Tmbreport, Labreport, Kalimpreport
from .reportmakerclass import TalambanRef, LabangonRef, KalimpyoRef
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


def getYesterday(date_string):
    now = date(*map(int, date_string.split('-')))
    yesterday = datetime.strftime(now - timedelta(1), '%Y-%m-%d')
    return yesterday


def uli(request):
    context = {}
    return render(request, 'businessreport/home.html', context)


def about(request):
    context = {}
    return render(request, 'businessreport/about.html', context)


@login_required(login_url='businessreport:login')
@allowed_users(allowed_roles=["talamban"])
def tmbindex(request):
    context = {}
    return render(request, 'businessreport/tmb_rep.html', context)


@login_required(login_url='businessreport:login')
@allowed_users(allowed_roles=["labangon"])
def labindex(request):
    context = {}
    return render(request, 'businessreport/lab_rep.html', context)


@login_required(login_url='businessreport:login')
@allowed_users(allowed_roles=["kalimpyo"])
def kalindex(request):
    context = {}
    return render(request, 'businessreport/kalimp_rep.html', context)


@login_required(login_url='businessreport:login')
def moonindex(request):
    context = {}
    return render(request, 'businessreport/moonlit_rep.html', context)


@login_required(login_url='businessreport:login')
def detail(request):
    # display all post values for debugging
    for key, value in request.POST.items():
        print('Key: %s' % (key))
        print('Value %s' % (value))
    if request.POST["location"] == "Talamban":
        tmbRef = TalambanRef(request.POST, request.user.groups.all()[0].name)
        tmbRef.modifyDB()
        context = tmbRef.postToContext()
    elif request.POST["location"] == "Labangon":
        labRef = LabangonRef(request.POST, request.user.groups.all()[0].name)
        labRef.modifyDB()
        context = labRef.postToContext()
    elif request.POST["location"] == "Kalimpyo":
        kalRef = KalimpyoRef(request.POST, request.user.groups.all()[0].name)
        kalRef.modifyDB()
        context = kalRef.postToContext()
    return render(request, 'businessreport/detail_rep.html', context)


def get_data_yesterday(request):
    print(request.POST['dateReport'])
    if request.POST["location"] == "Talamban":
        tmbRef = TalambanRef(request.POST, request.user.groups.all()[0].name)
        jsonData = tmbRef.ajax_yesterday()
        return JsonResponse(jsonData)
    elif request.POST["location"] == "Labangon":
        labRef = LabangonRef(request.POST, request.user.groups.all()[0].name)
        jsonData = labRef.ajax_yesterday()
        return JsonResponse(jsonData)
    elif request.POST["location"] == "Kalimpyo":
        kalRef = KalimpyoRef(request.POST, request.user.groups.all()[0].name)
        jsonData = kalRef.ajax_yesterday()
        return JsonResponse(jsonData)
    else:
        return JsonResponse({})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('businessreport:uli')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            dictUser = {"talamban": "tmbrep",
                        "labangon": "labrep", "kalimpyo": "kalrep", "admin": "uli"}
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                group = user.groups.all()[0].name
                return redirect('businessreport:{0}'.format(dictUser[group]))
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('businessreport:login')
