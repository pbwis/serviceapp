from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Call, Printer, Customer
from django.contrib.auth.decorators import login_required
from .forms import CreateCall, CreatePrinter, CreateCustomer
from . import forms


@login_required(login_url='/accounts/login')
def calls_list(request):
    calls = Call.objects.all().order_by('-date_start')
    printers = Printer.objects.all()
    return render(request, 'calls/calls_list.html', {'calls': calls, 'printers': printers})


@login_required(login_url='/accounts/login')
def call_detail(request, slug):
    call = Call.objects.get(slug=slug)
    customers = Customer.objects.all()
    printers = Printer.objects.all()
    return render(request, 'calls/call_detail.html', {'call': call, 'customers': customers, 'printers': printers})


@login_required(login_url='/accounts/login')
def call_create(request, slug):
    form = CreateCall(request.POST or None, request.FILES or None)
    printer = get_object_or_404(Printer, slug=slug)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.printer = printer
        instance.author = request.user
        instance.save()
        return HttpResponseRedirect(reverse('calls:printer_detail', args=(slug,)))

    return render(request, 'calls/call_create.html', {'form': form, 'printer': printer})


@login_required(login_url='/accounts/login')
def call_delete(request, slug):
    call = get_object_or_404(Call, slug=slug)
    if request.method == "POST":
        form = forms.DeleteCall(request.POST, request.FILES, instance=call)
        if form.is_valid():
            call = form.save(commit=False)
            call.author = request.user
            call.delete()
            return redirect('calls:list')
    else:
        form = forms.DeleteCall(instance=call)
    return render(request, 'calls/call_delete.html', {'call': call, 'form': form})


@login_required(login_url='/accounts/login')
def customer_create(request):
    if request.method == 'POST':
        form = forms.CreateCustomer(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('calls:customer_list')
    else:
        form = forms.CreateCustomer()

    return render(request, 'calls/customer_create.html', {'form': form})


@login_required(login_url='/accounts/login')
def printer_create(request, slug):
    form = CreatePrinter(request.POST or None, request.FILES or None)
    customer = get_object_or_404(Customer, slug=slug)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.customer = customer
        instance.author = request.user
        instance.save()
        return redirect('calls:printer_list')

    return render(request, 'calls/printer_create.html', {'form': form, 'customer': customer})


@login_required(login_url='/accounts/login')
def printer_detail(request, slug):
    printer = Printer.objects.get(slug=slug)
    calls = Call.objects.all().order_by('-date_start')
    customer = Customer.objects.all()
    return render(request, 'calls/printer_detail.html', {'printer': printer, 'calls': calls, 'customer': customer})


@login_required(login_url='/accounts/login')
def customer_list(request):
    customers = Customer.objects.all().order_by('-name')
    return render(request, 'calls/customer_list.html', {'customers': customers})


@login_required(login_url='/accounts/login')
def customer_detail(request, slug):
    customer = Customer.objects.get(slug=slug)
    printers = Printer.objects.all()
    if customer == printers:
        return render(request, 'calls/customer_detail.html', {'printers': printers})
    return render(request, 'calls/customer_detail.html', {'customer': customer, 'printers': printers})
