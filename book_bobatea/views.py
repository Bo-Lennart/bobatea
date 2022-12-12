from django.shortcuts import render, redirect, get_object_or_404
from .models import TeaMenu, AboutUs, StaffCrew, Reservation
from .forms import ReserveTableForm, add_item_to_menu_form

# Create your views here.

def get_menu(request):
    menu = TeaMenu.objects.all()

    context = {'menu': menu}

    return render(request, '../templates/base.html', context)


def staff_reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
        return redirect(staff_page)

    context = {'form': reserve_form}

    return render(request, '../templates/staff_reservation.html', context)


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

    return render(request, '../templates/contact.html', )


def staff_page(request):
    menu = TeaMenu.objects.all()
    reservations = Reservation.objects.all()

    context = {'menu': menu,
    'reservations': reservations
    }

    return render(request, '../templates/staff_page.html', context)


def add_menu_item(request):
    add_item = add_item_to_menu_form()

    if request.method == 'POST':
        add_item = add_item_to_menu_form(request.POST)
        if add_item.is_valid():
            add_item.save()
        return redirect(staff_page)

    context = {'add_item': add_item}

    return render(request, '../templates/add_menu_item.html', context)


def edit_menu(request, TeaMenu_id):
    item = get_object_or_404(TeaMenu, id=TeaMenu_id)
    form = add_item_to_menu_form(instance=item)
    context = {
        'form': form
    }

    return render(request, '../templates/edit_menu.html', context)


def edit_reservation(request, Reservation_id):
    booking = get_object_or_404(Reservation, id=Reservation_id)
    form = ReserveTableForm(instance=booking)
    context = {
        'form': form
    }

    return render(request, '../templates/edit_reservation.html', context)
