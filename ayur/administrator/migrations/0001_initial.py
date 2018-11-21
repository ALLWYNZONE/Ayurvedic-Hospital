# Generated by Django 2.1.2 on 2018-10-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dep_id', models.IntegerField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=300, unique=True)),
                ('dep_des', models.TextField(max_length=600, unique=True)),
                ('dep_image', models.ImageField(blank=True, upload_to='administrator/static/Departments/')),
            ],
        ),
    ]
