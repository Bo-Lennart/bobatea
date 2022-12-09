from django.shortcuts import render
from .models import TeaMenu, Reservation

# Create your views here.


def get_menu(request):
    menu = TeaMenu.objects.all()

    context = {'menu': menu}

    return render(request, '../templates/base.html', context)


def reserve_table(request):
    return render(request, '../templates/reservation.html', name='reserv_table')
    