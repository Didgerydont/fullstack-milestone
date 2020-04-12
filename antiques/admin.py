from django.contrib import admin
from .models import Antiques, Enquire


class EnquireAdmin(admin.ModelAdmin):
    fields = ('title', 'antiques', 'time_requested', 'enquiry', 'solved')


admin.site.register(Antiques)
admin.site.register(Enquire, EnquireAdmin)