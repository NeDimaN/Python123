from django.urls import path
from .views import *


urlpatterns = [
    path('', MainHome.as_view(), name='index'),
    # path('race/', ActiveHome.as_view(), name='race'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),

]

