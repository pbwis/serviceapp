from django.urls import path
from . import views

app_name = 'calls'

urlpatterns = [
    path('', views.calls_list, name='list'),
    path('<slug>/', views.call_detail, name='detail')
]