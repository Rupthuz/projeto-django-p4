from django.shortcuts import render
from django.http import HttpResponse


def customers(request):
    return render(request, 'customers.html')