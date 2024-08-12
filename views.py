from urllib import request
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponse, HttpResponseBadRequest
from .models import Product,Department,Staff,Store,Transaction


# Create your views here.
def index(request):
    data = Product.objects.all()
    context_data = {'data':data}
    return render(request, "store_app/index.html",context_data)

def ledger(request):
    return render(request,"store_app/ledger.html")

def order(request):
    return render(request,"store_app/order.html")

def product(request,id):

    return render(request,"store_app/product-list.html")

def detail(request,id):
    detail = Product.objects.get(id=id)
    context_data = {'detail':detail}
    return render(request,"store_app/detail.html",context_data)

def About(request):
    data = Department.objects.all()
    context_data = {'data':data}
    return render(request,"store_app/about.html",context_data)

def Feature(request):
    return render(request,"store_app/features.html")

def login(request):
    return render(request,"store_app/login.html")

def register(request):
    return render(request,"store_app/register.html")

def report(request):
    return render(request,"store_app/reports.html")
