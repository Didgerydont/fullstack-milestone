from django.contrib import admin
from .models import PastSold, ItemRequest, RequestedItemAdmin

admin.site.register(PastSold)
admin.site.register(ItemRequest)
admin.site.register(RequestedItemAdmin)
