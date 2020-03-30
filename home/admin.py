from django.contrib import admin
from .models import PastSold, ItemRequest
from django.utils.safestring import mark_safe


class ItemRequestAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    def image_tag(self):
        # used in the admin site model as a "thumbnail"
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()))

    image_tag.short_description = 'Image'
    
    fields = (
        'name',
        'description',
        'image',
    )
    readonly_fields = (
        'image_tag',
        'name',
        'description',
        'image',
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


admin.site.register(ItemRequest, ItemRequestAdmin)

admin.site.register(PastSold)