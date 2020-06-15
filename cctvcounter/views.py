from django.shortcuts import render
from .decorators import *
# Create your views here.


@allowed_users(allowed_roles=["admin"])
def cctvgolde(request):
    context = {}
    return render(request, 'cctvcounter/cctvgolde.html', context)


@allowed_users(allowed_roles=["admin"])
def cctvrefill(request):
    context = {}
    return render(request, 'cctvcounter/cctvrefilling.html', context)


def refloadsave(request):
    pass
