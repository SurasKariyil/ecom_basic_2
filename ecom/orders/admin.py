from django.contrib import admin
from orders.models import OrderedItem,Order

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        'owner',
        'order_status',
    ]
    search_fields = [
        'owner',
        'id'
    ]
# Register your models here.
admin.site.register(Order,OrderAdmin)
