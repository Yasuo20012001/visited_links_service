from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('visited_links.urls')),
    path('', lambda request: redirect('visited_links/')),
]
