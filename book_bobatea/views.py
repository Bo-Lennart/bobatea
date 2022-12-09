from django.shortcuts import render
from .models import TeaMenu
from .forms import ReserveTableForm

# Create your views here.


def get_menu(request):
    menu = TeaMenu.objects.all()

    context = {'menu': menu}

    return render(request, '../templates/base.html', context)


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.method)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}

    return render(request, '../templates/reservation.html', context)
