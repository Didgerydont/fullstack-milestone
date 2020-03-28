from django.contrib import admin
from .models import PastSold, ItemRequest


class ItemRequestAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = (
        'image_tag',
        'name',
        'description',
        'image',
        'externalURL',
    )
    readonly_fields = ('image_tag',)
    list_display = (
        'name',
        'description',
        'budget',
        'contact',
        'request_date',
    )


admin.site.register(ItemRequest, ItemRequestAdmin)

admin.site.register(PastSold)