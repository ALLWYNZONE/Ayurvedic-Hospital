from django.contrib import admin

# Register your models here.
from.models import Departments
admin.site.register(Departments)
admin.site.site_header = 'Ayur Hospital Administration'
from.models import (Doctor)
admin.site.register(Doctor)
from.models import Category
admin.site.register(Category)
from.models import(Medicines)
admin.site.register(Medicines)
from.models import (Stock)
admin.site.register(Stock)

