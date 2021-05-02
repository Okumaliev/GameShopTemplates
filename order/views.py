from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateOrderForm
from main1.models import Game

def order(reuqest):
    return HttpResponse('Hello')

def create_order(request, game_id):
    game = Game.objects.get(id=game_id)
    order_form = CreateOrderForm(request.POST)
    if order_form.is_valid():
        # print(order_form.cleaned_data)
        order_form.save()
        # return render(request, 'order/order.html', {'form': order_form},
        # {'game': game})
    order_form = CreateOrderForm()
    print('I am here')
    return render(request, 'order/order.html', {'form': order_form, 'game': game},)