# Generated by Django 3.2.9 on 2021-12-05 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211205_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Profile_image',
            new_name='profile_image',
        ),
    ]
