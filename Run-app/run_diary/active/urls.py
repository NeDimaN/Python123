from django.urls import path
from .views import *


urlpatterns = [
    path('', ActiveHome.as_view(), name='race'),
    path('part/<slug:part_slug>/', ShowPart.as_view(), name='part'),

]