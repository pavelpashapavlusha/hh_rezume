from django.urls import path

from . import views

app_name = 'about_app'

urlpatterns = [
    path('', views.about, name='about'),
]
