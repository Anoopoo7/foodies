from django.contrib import admin

from .models import products
from .models import orders
from .models import feedback
admin.site.register(products)
admin.site.register(orders)
admin.site.register(feedback)
