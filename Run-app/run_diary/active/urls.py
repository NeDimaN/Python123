from django.urls import path
from .views import *


urlpatterns = [
    path('', ActiveHome.as_view(), name='race'),
    path('part/<slug:part_slug>/', ShowPart.as_view(), name='part'),
    path('category/<slug:cat_slug>/', ActiveCategory.as_view(), name='category'),
    path('addpage/', AddPage.as_view(), name='add_page'),

]