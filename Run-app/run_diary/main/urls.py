from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', MainHome.as_view(), name='index'),
    # path('race/', ActiveHome.as_view(), name='race'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),



]

