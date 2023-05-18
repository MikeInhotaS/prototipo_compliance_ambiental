from django.urls import path
from . import views

urlpatterns=[
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_app, name='login_app'),
    path('logout/', views.logout_app, name='logout_app'),
    path('plataforma/', views.plataforma, name='plataforma'),
    path('plantas/', views.plantas, name='plantas'),
    path('detalhe_planta/<int:id_planta>', views.detalhe_planta, name='detalhe_planta'),
    path('projetos/', views.projetos, name='projetos'),
    path('criar_projeto/', views.criar_projeto, name='criar_projeto')
]