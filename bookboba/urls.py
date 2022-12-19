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
from book_bobatea import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_menu, name='menu'),
    path('reservation/', views.reserve_table, name='reserve_table'),
    path('about_us/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('staff_page/', views.staff_page, name='staff'),
    path('accounts/', include('allauth.urls')),
    path('add_item_to_menu/', views.add_menu_item, name='add_menu_item'),
    path('staff_reservation/', views.staff_reserve_table, name='staff_reserve_table'),
    path('edit/<TeaMenu_id>/', views.edit_menu, name='edit_menu'),
    path('edit_reservation/<Reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete/<TeaMenu_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('remove/<Reservation_id>/', views.remove_reservation, name='remove_reservation'),
    path('reservation_confirmation/', views.reservation_confirmation, name='confirmation_page'),
    path('delete_cancelation/<CancelReservation_id>', views.delete_cancelation, name='delete_cancelation')
]