# Generated by Django 2.1.2 on 2018-10-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='dep_des',
            field=models.TextField(max_length=6000000, unique=True),
        ),
    ]
