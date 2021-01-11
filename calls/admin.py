from django.contrib import admin
from .models import Call, Printer, Customer


admin.site.register(Call)
admin.site.register(Printer)
admin.site.register(Customer)