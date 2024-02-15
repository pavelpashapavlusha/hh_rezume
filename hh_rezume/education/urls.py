from django.urls import path

from . import views

app_name = 'education_app'

urlpatterns = [
    path('', views.education, name='education'),
]
