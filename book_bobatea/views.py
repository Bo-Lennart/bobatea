from django.shortcuts import render
from .models import TeaMenu

# Create your views here.


def get_home_page(request):
    menu = TeaMenu.objects.all()
    context = {
        'items': menu
    }
    return render(request, '../templates/index.html', context)
