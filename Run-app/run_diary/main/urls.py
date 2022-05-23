from django.urls import path
from .views import *


urlpatterns = [
    path('', MainHome.as_view(), name='index'),
    # path('race/', ActiveHome.as_view(), name='race'),

]
