# Generated by Django 2.1.3 on 2018-11-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0010_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saveappointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(max_length=30)),
                ('addresss', models.TextField(max_length=50)),
                ('todaysdate', models.DateField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField()),
                ('doc', models.TextField(max_length=30)),
                ('disease', models.TextField(max_length=50)),
            ],
        ),
    ]
