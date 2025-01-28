from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Inclui as URLs da app accounts
    path('', include('core.urls')),  # Inclui as URLs do aplicativo core
    
]
