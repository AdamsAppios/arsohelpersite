from django.shortcuts import render
from .decorators import *
from django.http import JsonResponse
from .cctvfunctions import *

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
    post = request.POST
    modelClass = chooseClass(post["location"])
    d = {
        "timeCC": post["timeCC"],
        "dealer": post["dealer"],
        "pickup": post["pickup"],
        "smallGal": post["smallGal"],
        "rnd": post["rnd"],
        "squareGal": post["squareGal"],
        "dealCust": post["dealCust"],
        "dayparts": post["dayparts"],
        "suspectText": post["suspectText"],
    }
    if post["option"] == "save":
        try:
            mdlRow = modelClass.objects.get(date__exact=post["date"])
        except (KeyError, modelClass.DoesNotExist):
            print("creating new object")
            d["date"] = post["date"]
            mdlRow = modelClass(**d)
            mdlRow.save()
        else:
            print("updating date")
            modelClass.objects.filter(
                date__exact=post["date"]).update(**d)
        return JsonResponse({})
    elif post["option"] == "load":
        try:
            mdlRow = modelClass.objects.get(date__exact=post["date"])
        except (KeyError, modelClass.DoesNotExist):
            pass
        else:
            data = {
                "timeCC": mdlRow.timeCC,
                "dealer": mdlRow.dealer,
                "pickup": mdlRow.pickup,
                "rnd": mdlRow.rnd,
                "smallGal": mdlRow.smallGal,
                "squareGal": mdlRow.squareGal,
                "dealCust": mdlRow.dealCust,
                "suspectText": mdlRow.suspectText,
                "dayparts": mdlRow.dayparts,
            }
            return JsonResponse(data)
    else:
        return JsonResponse({})


def goldloadsave(request):
    pass
