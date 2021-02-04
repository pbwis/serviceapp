from django.urls import path
from . import views

app_name = 'calls'

urlpatterns = [
    path('', views.calls_list, name='list'),
    path('<slug>/', views.call_detail, name='detail'),
    path('<slug>/edit/', views.call_edit, name='edit'),
    path('<slug>/delete/', views.call_delete, name='delete'),
    path('printer/<slug>/create', views.call_create, name='create'),
    path('customer/<slug>/create/', views.printer_create, name='printer_create'),
    path('printer/<slug>/', views.printer_detail, name='printer_detail'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/', views.customer_list, name='customer_list'),
    path('customer/<slug>/', views.customer_detail, name='customer_detail'),
]