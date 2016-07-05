# -*- coding: utf-8 -*- #

from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from lunchSelector.models import Menu,Order
from datetime import datetime
from random import randint


def show_index(request):
    menus = Menu.objects.all()

    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    return render(request,'index.html',{'menus':menus,'date':now_date})

def submit(request):

    if request.POST:

        print request.POST

        selected_menu_text = request.POST['choice']

        selected_menu = Menu.objects.get(menu_text=selected_menu_text)
        selected_menu.count += 1
        selected_menu.count_permanent += 1

        new_order = Order()
        new_order.o_menu_text = selected_menu.menu_text
        new_order.date = datetime.now().strftime("%Y-%m-%d")
        selected_menu.save()
        new_order.save()
    else:
        return HttpResponse("밥을 골라!")

    return HttpResponse("맛점!")

def show_results(request):
    today_date = datetime.now().strftime("%Y-%m-%d")
    order_list = Order.objects.filter(date=today_date)

    order_menu=[]


    for order in order_list:
        order_menu.append(Menu.objects.get(menu_text=order.o_menu_text))



    return render(request,'results.html',{'order_menu':set(order_menu)})


def reset(request):
    menus = Menu.objects.all()

    for menu in menus:
        menu.count = 0
        menu.count_permanent -= 1
        menu.save()


    return HttpResponseRedirect('/results/')

def save_data(request):
    menus = Menu.objects.all()

    for menu in menus:
        menu.count = 0
        menu.save()

    return HttpResponseRedirect('/results/')



def view_count(request):
    menus = Menu.objects.all()

    random_number = randint(0,len(menus))
    print random_number


    return render(request,'results_count.html',{'menus':menus})



def menu_chooser(request):
    menus = Menu.objects.all()

    random_number = randint(0,len(menus))



    return HttpResponse("success")







# Create your views here.
