from django.contrib import admin
from .models import PastSold, ItemRequest


class ItemRequestAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'description',
        'budget',
        'image_tag',
        'contact',
        'request_date',
    )


admin.site.register(ItemRequest, ItemRequestAdmin)

admin.site.register(PastSold)