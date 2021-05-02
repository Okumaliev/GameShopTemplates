from django.urls import path

from order.views import create_order

urlpatterns = [
    path('create/<int:game_id>', create_order, name='create-order'),

]