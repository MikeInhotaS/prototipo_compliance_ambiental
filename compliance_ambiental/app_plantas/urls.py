from django.urls import path
from . import views

urlpatterns=[
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_app, name='login_app'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('plantas/', views.plantas, name='plantas')
]