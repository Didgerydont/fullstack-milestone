from django.contrib import admin
from .models import Antiques, Enquire


class AntiquesAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_posted', 'bought')
    list_filter = ('name', 'date_posted', 'bought')


admin.site.register(Antiques, AntiquesAdmin)


class EnquireAdmin(admin.ModelAdmin):
    list_display = ('antiques', 'user', 'time_requested', 'solved')
    list_filter = ('time_requested', 'user')


admin.site.register(Enquire, EnquireAdmin)
