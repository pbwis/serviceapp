from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, datetime
import uuid


class EstTimeChoice(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return str(self.description)


class EstTimeProfile(models.Model):
    choices = models.ManyToManyField(EstTimeChoice)


class TypeOfEstTime(models.Model):
    thirty = '0h 30min'
    fortyfive = '0h 45min'
    sixty = '1h 00min'
    seventyfive = '1h 15min'
    ninety = '1h 30min'
    hundredfive = '1h 45min'
    hundredtwenty = '2h 00min'
    hundredtwentyplus = '2h +'
    TYPE_OF_ESTTIME_CHOICES = [
        (thirty, '0h 30min'),
        (fortyfive, '0h 45min'),
        (sixty, '1h 00min'),
        (seventyfive, '1h 15min'),
        (ninety, '1h 30min'),
        (hundredfive, '1h 45min'),
        (hundredtwenty, '2h 00min'),
        (hundredtwentyplus, '2h +'),
    ]
    type_of_esttime = models.CharField(
        max_length=50,
        choices=TYPE_OF_ESTTIME_CHOICES,
        default=thirty
    )

    description_of_time = models.CharField(max_length=50)

    def __str__(self):
        return str(self.description_of_time)


class Copier(models.Model):
    cop_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cop_name


class CopTypeChoice(models.Model):
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.description


class CopTypeProfile(models.Model):
    choices = models.ManyToManyField(CopTypeChoice)


class TypeOfDevice(models.Model):
    HIGHVOLCC = 'High Volume COLOUR copier'
    HIGHVOLMC = 'High Volume MONO copier'
    MIDVOLCC = 'Mid Volume COLOUR copier'
    MIDVOLMC = 'Mid Volume MONO copier'
    PRMON = 'Printer MONO'
    PRCOL = 'Printer COLOUR'
    MFPMON = 'Multifunction MONO'
    MFPCOL = 'Multifunction COLOUR'
    BARPR = 'Barcode Printer'
    TYPE_OF_DEVICE_CHOICES = [
        (HIGHVOLCC, 'High Volume COLOUR copier'),
        (HIGHVOLMC, 'High Volume MONO copier'),
        (MIDVOLCC, 'Mid Volume COLOUR copier'),
        (MIDVOLMC, 'Mid Volume MONO copier'),
        (PRMON, 'Printer MONO'),
        (PRCOL, 'Printer COLOUR'),
        (MFPMON, 'Multifunction MONO'),
        (MFPCOL, 'Multifunction COLOUR'),
        (BARPR, 'Barcode Printer'),
    ]
    type_of_device = models.CharField(
        max_length=50,
        choices=TYPE_OF_DEVICE_CHOICES,
        default=MIDVOLCC,
    )

    device_name = models.CharField(max_length=50)

    def __str__(self):
        return self.device_name


class Copier(models.Model):
    cop_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cop_name


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

    def date_end(self):
        if self.date_estimate == TypeOfEstTime.thirty:
            return self.date_start + timedelta(minutes=30, hours=0)
        elif str(self.date_estimate) == TypeOfEstTime.fortyfive:
            return self.date_start + timedelta(minutes=45, hours=0)
        elif str(self.date_estimate) == TypeOfEstTime.sixty:
            return self.date_start + timedelta(minutes=0, hours=1)
        elif str(self.date_estimate) == TypeOfEstTime.seventyfive:
            return self.date_start + timedelta(minutes=15, hours=1)
        elif str(self.date_estimate) == TypeOfEstTime.ninety:
            return self.date_start + timedelta(minutes=30, hours=1)
        elif str(self.date_estimate) == TypeOfEstTime.hundredfive:
            return self.date_start + timedelta(minutes=45, hours=1)
        elif str(self.date_estimate) == TypeOfEstTime.hundredtwenty:
            return self.date_start + timedelta(minutes=0, hours=2)
        elif str(self.date_estimate) == TypeOfEstTime.hundredtwentyplus:
            return self.date_start + timedelta(minutes=30, hours=2)
        else:
            return str("Incorrect date format")