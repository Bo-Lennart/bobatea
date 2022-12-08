from django.shortcuts import render
from .models import TeaMenu

# Create your views here.


def get_menu(request):
    menu = TeaMenu.objects.all()

    context = {'menu': menu}

    return render(request, '../templates/base.html', context)
