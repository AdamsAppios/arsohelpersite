from django.shortcuts import render

# Create your views here.


def capsealCnt(request):
    context = {}
    return render(request, 'js_apps/capsealcnt.html', context)


def moneyCnt(request):
    context = {}
    return render(request, 'js_apps/moneycnt.html', context)
