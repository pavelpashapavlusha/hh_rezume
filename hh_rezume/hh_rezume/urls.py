from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('about/', include('about.urls')),
    path('education/', include('education.urls')),
    path('work/', include('work.urls')),
    path('sertificate/', include('sertificate.urls')),
]
