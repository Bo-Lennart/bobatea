# Generated by Django 3.2.16 on 2022-12-08 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_bobatea', '0002_alter_teamenu_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamenu',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
