# Generated by Django 5.0.6 on 2024-06-07 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_remove_plan_date_remove_plan_time'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plan',
            new_name='Todo',
        ),
    ]
