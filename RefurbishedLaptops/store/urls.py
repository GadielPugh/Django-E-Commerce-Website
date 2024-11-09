from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('gallery/', views.laptop_gallery, name='gallery'),
    path('laptop/<int:id>/', views.laptop_detail, name='laptop_detail'),
    path('purchase/<int:laptop_id>/', views.purchase_laptop, name='purchase_laptop'),
    path('purchase_success/', views.purchase_success, name='purchase_success'),
]