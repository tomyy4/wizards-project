

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api/', include('wizards_api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
