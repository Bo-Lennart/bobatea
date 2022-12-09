from django.shortcuts import render
from .models import TeaMenu, AboutUs, StaffCrew
from .forms import ReserveTableForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def get_menu(request):
    menu = TeaMenu.objects.all()

    context = {'menu': menu}

    return render(request, '../templates/base.html', context)


def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    context = {'form': reserve_form}

    return render(request, '../templates/reservation.html', context)


def about(request):
    about = AboutUs.objects.last()
    staff_crew = StaffCrew.objects.last()

    context = {
        'about': about,
        'staff_crew': staff_crew,
    }

    return render(request, '../templates/about_us.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, '../templates/contact.html', context)


def send_success(request):
    pass
