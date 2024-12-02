# urls.py
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('colegios/', views.colegio_list, name='colegio_list'),
    path('measurementcreate/', csrf_exempt(views.estudiante_create), name='estudianteCreate'),
    path('estudiante/<int:pk>/delete/', views.estudiante_delete, name='estudiante_delete'),
]