# Generated by Django 3.2.16 on 2022-12-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_bobatea', '0005_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='about_us/')),
            ],
        ),
        migrations.CreateModel(
            name='StaffCrew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='staff_crew/')),
            ],
        ),
    ]
