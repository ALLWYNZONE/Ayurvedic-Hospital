# Generated by Django 2.1.2 on 2018-11-08 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_auto_20181108_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='med_name',
            new_name='med_id',
        ),
    ]
