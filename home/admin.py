from django.contrib import admin
from .models import PastSold, ItemRequest



class ItemRequestAdmin(admin.ModelAdmin):  
    fields = (
        'name',
        'description',
        'image_tag',
        'contact',
    )
    readonly_fields = (
        'image_tag',
        'name',
        'description',
        'image_tag',
        'contact',
    )
    list_display = (
        'image_tag',
        'name',
        'description',
        'budget',
        'contact',
        'request_date',
    )
    exclude = (
        'image',
    )


admin.site.register(ItemRequest, ItemRequestAdmin)

admin.site.register(PastSold)