from django.urls import path
from . import views

urlpatterns = [
    path('', views.componentes_list, name='componentes_list'),
    path('crear/', views.componente_create, name='componente_create'),
    path('eliminar/<int:pk>', views.componente_delete, name='componente_delete'),
    path('reactivar/<int:pk>', views.componente_reactivar, name='componente_reactivar'),
]
