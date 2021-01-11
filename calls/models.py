from django.db import models
from django.contrib.auth.models import User
import uuid


class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    post_code = models.CharField(max_length=10)
    note = models.TextField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(unique=False)

    def __str__(self):
        return str(self.name)


class Printer(models.Model):
    name = models.CharField(max_length=100)
    ser_num = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, default=None, on_delete=models.CASCADE)
    slug = models.SlugField(unique=False)

    def __str__(self):
        return str(self.name) + ' - S/N: ' + self.ser_num


class Call(models.Model):
    printer = models.ForeignKey(Printer, default=None, on_delete=models.SET_NULL, null=True)
    page_count_b = models.IntegerField(default=0)
    page_count_c = models.IntegerField(default=0)
    error_code = models.CharField(max_length=100, null=True, blank=True)
    action = models.TextField(max_length=1000, null=True, blank=True)
    external_number = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    date_finish = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    expenses = models.FloatField(max_length=10, default=0.00)
    slug = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for call')
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    thumb = models.ImageField(upload_to='media/', default='default.png')

    def __str__(self):
        return str(self.printer.name)

    def snippet(self):
        return self.action[:50] + '...'

    def work_time(self):
        return self.date_finish - self.date_start

    def total_page(self):
        return int(self.page_count_b) + int(self.page_count_c)
