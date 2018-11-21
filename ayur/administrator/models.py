from django.db import models


class Departments(models.Model):
    dep_id = models.AutoField(primary_key=True)
    dep_name = models.CharField(max_length=300, unique=True)
    dep_des = models.TextField(max_length=6000000, unique=True)
    dep_image = models.ImageField(upload_to='administrator/static/Departments/', blank=True)

    def __str__(self):
        return self.dep_name

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.cat_name

class Medicines(models.Model):
    med_id = models.AutoField(primary_key=True)
    cat_id = models.ForeignKey('Category', on_delete=models.ForeignKey)
    med_name = models.CharField(max_length=300, unique=True)
    med_image = models.ImageField(upload_to='administrator/static/Medicines/', blank=True)

    def __str__(self):
        return self.med_name

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    med_id = models.ForeignKey('Medicines', on_delete=models.ForeignKey)
    stock_name = models.TextField(max_length=50)
    batch_no = models.TextField(max_length=20)
    mfd_date = models.DateField()
    exp_date = models.DateField()
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.stock_name





class Doctor(models.Model):
    doct_id = models.AutoField(primary_key=True)
    doct_name = models.CharField(max_length=300, unique=True)
    dep_id = models.ForeignKey('Departments', on_delete=models.ForeignKey)
    qualification = models.TextField(max_length=600)
    specializations = models.TextField(max_length=300)
    doct_des = models.TextField(max_length=6000000, unique=True)
    doct_image = models.ImageField(upload_to='administrator/static/Doctors/', blank=True)
    status = models.TextField(max_length=100)

    def __str__(self):
        return self.doct_name





class Saveappointment(models.Model):
    fullname=models.TextField(max_length=30)
    addresss=models.TextField(max_length=50)
    todaysdate=models.DateField()
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField()
    doc=models.TextField(max_length=30)
    disease=models.TextField(max_length=50)


class login(models.Model):
    username= models.TextField(max_length=50)
    password= models.TextField(max_length=50)
    role=models.TextField(max_length=50)

class patientaccount(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField(max_length=50)


class contactus(models.Model):
    name=models.CharField(max_length=40)
    email=models.TextField()
    subject=models.TextField()
    message=models.TextField