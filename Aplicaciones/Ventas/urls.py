from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('registrarLibro/', views.registrarLibro),
    path('edicionLibro/<codigo>', views.edicionLibro),
    path('editarLibro/', views.editarLibro),
    path('eliminacionLibro/<codigo>', views.eliminacionLibro) 
]
