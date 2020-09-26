from django.urls import path
from . import views

app_name = 'app1'

urlpatterns = [
    path('help/', views.help, name='help'),
    path('sp/', views.sp, name='sp'),
    path('calculadora/', views.calculadora, name='calculadora'),
    path('acesso/', views.acesso, name='acesso'),
    path('form/', views.form_name, name='form'),
    path('modelform/', views.users, name='modelform'),
]