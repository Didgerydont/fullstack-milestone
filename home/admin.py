from django.contrib import admin
from .models import PastSold, ItemRequest



class ItemRequestAdmin(admin.ModelAdmin):  
    """
    Item request admin allows us to view the image that the user uploads with their request. 
    """
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