from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('calls/', include('calls.urls'))
]

urlpatterns += staticfiles_urlpatterns()