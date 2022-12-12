from django.db import models
from django.utils.text import slugify
from django import forms


# Create your models here.


class TeaMenu(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    quantity = models.IntegerField()
    price = models.IntegerField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(TeaMenu, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tea Menu'
        verbose_name_plural = 'Tea Menu'


class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
        


class AboutUs(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.name


class StaffCrew(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Staff Crew'
        verbose_name_plural = 'Staff Crew'

    def __str__(self):
        return self.name
