from django.contrib import admin

# Register your models here.

from .models import TeaMenu, Reservation


admin.site.register(TeaMenu)
admin.site.register(Reservation)