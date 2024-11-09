"""
URL configuration for RefurbishedLaptops project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# RefurbishedLaptops/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store import views  # Ensure your views are imported
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('gallery'), name='home'),  # Redirect root URL to gallery
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('gallery/', views.laptop_gallery, name='gallery'),
    path('purchase/<int:laptop_id>/', views.purchase_laptop, name='purchase'),
    path('laptops/<int:laptop_id>/', views.laptop_detail, name='laptop_detail'),
    path('purchase/success/', views.purchase_success, name='purchase_success'),
    path('logout/', views.custom_logout, name='logout'),
    path('purchase_confirmation/<int:transaction_id>/', views.purchase_confirmation, name='purchase_confirmation'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
