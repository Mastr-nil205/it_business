from django.urls import path

from . import views


app_name = 'premiere_nuage'
urlpatterns = [
    path('', views.home, name='home'),
]
