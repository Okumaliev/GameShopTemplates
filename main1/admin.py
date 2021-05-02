from django.contrib import admin

from main1.models import *
from order.models import *

admin.site.register(Type)
admin.site.register(Game)
admin.site.register(Order)
