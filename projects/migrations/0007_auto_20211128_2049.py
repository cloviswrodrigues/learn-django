# Generated by Django 3.2.9 on 2021-11-28 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='vale_ratio',
            new_name='vote_ratio',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='vale_total',
            new_name='vote_total',
        ),
    ]