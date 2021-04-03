from django.urls import path
from . import views

app_name = 'calls'

urlpatterns = [
    path('printer/results/', views.search_printer, name='search_printer'),
    path('customer/results/', views.search_customer, name='search_customer'),
    path('customer/', views.customer_list, name='customer_list'),
    path('customer/create/', views.customer_create, name='customer_create'),
    path('customer/<slug>/', views.customer_detail, name='customer_detail'),
    path('printer/', views.printer_list, name='printer_list'),
    path('customer/<slug>/create/', views.printer_create, name='printer_create'),
    path('copier/', views.copier_list, name='copier_list'),
    path('copier/create/', views.copier_create, name='copier_create'),
    path('esttime/', views.esttime_list, name='esttime_list'),
    path('esttime/create/', views.esttime_create, name='esttime_create'),
    path('printer/<slug>/', views.printer_detail, name='printer_detail'),
    path('send/', views.mail_from_web, name='mail_from_web'),
    # path('expenses/', views.product_list, name='expenses'),
    path('printer/<slug>/create/', views.call_create, name='create'),
    path('', views.calls_list, name='list'),
    path('results/', views.search, name='search'),
    path('<slug>/', views.call_detail, name='detail'),
    path('<slug>/edit/', views.call_edit, name='edit'),
    path('<slug>/delete/', views.call_delete, name='delete'),
    path('export/csv/', views.export_call_csv, name='export_call_csv'),
]