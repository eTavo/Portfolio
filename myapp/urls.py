from django.urls import path
from .views import inicio, index, about, projects, exit

urlpatterns = [
    path('', inicio, name='inicio'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('logout/', exit, name='exit'),
]