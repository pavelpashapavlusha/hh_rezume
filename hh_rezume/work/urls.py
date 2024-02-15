from django.urls import path

from . import views

app_name = 'work_app'

urlpatterns = [
    path('', views.work, name='work'),
]
