from django.contrib import admin

# Register your models here.

from .models import TeaMenu, Reservation, AboutUs, StaffCrew


admin.site.register(TeaMenu)
admin.site.register(Reservation)
admin.site.register(AboutUs)
admin.site.register(StaffCrew)
