from django.urls import path

from . import views

app_name = 'homepage_app'

urlpatterns = [
    path('', views.index, name='homepage'),
]
