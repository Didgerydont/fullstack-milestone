from django.contrib import admin
from django.utils.html import format_html
from .models import PastSold, ItemRequest


class ItemRequestAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
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