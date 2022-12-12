"""bookboba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from book_bobatea.views import get_menu, reserve_table, about, contact, staff_page, add_menu_item, staff_reserve_table, edit_menu, edit_reservation, delete_menu_item, remove_reservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_menu, name='menu'),
    path('reservation/', reserve_table, name='reserve_table'),
    path('about_us/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('staff_page/', staff_page, name='staff'),
    path('accounts/', include('allauth.urls')),
    path('add_item_to_menu/', add_menu_item, name='add_menu_item'),
    path('staff_reservation/', staff_reserve_table, name='staff_reserve_table'),
    path('edit/<TeaMenu_id>/', edit_menu, name='edit_menu'),
    path('edit_reservation/<Reservation_id>/', edit_reservation, name='edit_reservation'),
    path('delete/<TeaMenu_id>/', delete_menu_item, name='delete_menu_item'),
    path('remove/<Reservation_id>/', remove_reservation, name='remove_reservation'),
]