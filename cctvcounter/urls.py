from django.urls import path, include
from . import views
app_name = 'cctvcheckup'

urlpatterns = [
    path('cctv/goldeglo', views.cctvgolde, name='cctvgolde'),
    path('cctv/refilling', views.cctvrefill, name='cctvrefill'),
    path('cctv/ajax/refillingloadsave/', views.refloadsave, name='refloadsave'),
    path('cctv/ajax/goldloadsave/', views.goldloadsave, name='goldloadsave')
]
