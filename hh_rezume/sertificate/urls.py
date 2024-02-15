from django.urls import path

from . import views

app_name = 'sertificate_app'

urlpatterns = [
    path('', views.sertificate, name='sertificate'),
]
