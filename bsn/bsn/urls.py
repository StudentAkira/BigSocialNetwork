from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('auth', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
