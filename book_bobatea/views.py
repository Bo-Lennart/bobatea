from django.shortcuts import render
from .models import TeaMenu
from .forms import ReserveTableForm

# Create your views here.


def get_menu(request):
    menu = TeaMenu.objects.all()

    context = {'menu': menu}

    return render(request, '../templates/base.html', context)


def reserve_table(request):
  
    context = {}

    return render(request, '../templates/reservation.html', context)
