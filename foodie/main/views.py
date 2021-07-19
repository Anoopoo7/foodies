from django.shortcuts import render,redirect
from .functions import plp_func, home_func,product_func,order_func,search_fun,reg_form,log_func,feed_func


def login(request):
    return render(request, 'home/htmls/regLog.html')


def home(request):
    special = home_func(request)
    return render(request, 'home/htmls/home.html', {"special": special})


def product(request,id):
    if request.method == 'POST':
        res = order_func(request,id)
    item = product_func(id)
    return render(request, 'home/htmls/product.html',{'item':item})


def plp(request):
    if request.method == 'POST':
        data = search_fun(request)
    else:
        data = plp_func(request)
    return render(request, 'home/htmls/plp.html', {'data': data})


def contact(request):
    return render(request, 'home/htmls/contact.html')

def reg(request):
    if reg_form(request):
        print("ture")
        return redirect('/')
    else:
        print("false")
        msg = "Account is already created"
        return render(request, 'home/htmls/regLog.html',{"msg":msg})

def logger(request):
    if log_func(request):
        return render(request, 'home/htmls/home.html')
    else:
        msg = "Incorrected details"
        return render(request, 'home/htmls/regLog.html',{"msg":msg})

def feedback(request):
    data = feed_func(request)
    return render(request, 'home/htmls/contact.html',{"data":data})