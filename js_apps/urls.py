from django.urls import path, include
from . import views
app_name = 'js_app'
urlpatterns = [
    path('app/capsealcounter', views.capsealCnt, name='capsealcounter'),
    path('app/moneycounter', views.moneyCnt, name='moneycounter'),
    path('app/labreport', views.labReport, name="labreport")
]
