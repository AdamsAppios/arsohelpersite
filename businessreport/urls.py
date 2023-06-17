from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from . import views
app_name = 'businessreport'

urlpatterns = [
    path('bu/talamban/', views.tmbindex, name='tmbrep'),
    path('bu/labangon/', views.labindex, name='labrep'),
    path('bu/kalimpyo/', views.kalindex, name='kalrep'),
    path("bu/moonlit/", views.moonindex, name="moonrep"),
    path('detalye/', views.detail, name='detailrep'),
    path("ajax/get_data_yesterday/",
         views.get_data_yesterday, name='get_data_yesterday'),
    path('', views.uli, name='uli'),
    path('about/', views.about, name="about"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]
