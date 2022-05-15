from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    # Auth
    path('signup/', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    # Todos
    path('current/', views.currenttodos, name='currenttodos'),
]
