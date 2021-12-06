# Generated by Django 3.2.9 on 2021-12-01 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0007_auto_20211128_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]