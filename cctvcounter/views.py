from django.shortcuts import render

# Create your views here.


def cctvgolde(request):
    context = {}
    return render(request, 'cctvcounter/cctvgolde.html', context)


def cctvrefill(request):
    context = {}
    return render(request, 'cctvcounter/cctvrefilling.html', context)
