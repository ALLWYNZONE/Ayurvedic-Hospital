from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from administrator.models import login
from administrator.models import patientaccount
from administrator.models import Saveappointment
from administrator.models import contactus

# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def aboutus(request):
    template = loader.get_template('aboutus.html')
    return HttpResponse(template.render())
def ayurveda(request):
    template = loader.get_template('ayurveda.html')
    return HttpResponse(template.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
def departments(request):
    template = loader.get_template('departments.html')
    return HttpResponse(template.render())
def doctors(request):
    template = loader.get_template('doctors.html')
    return HttpResponse(template.render())
def appointment(request):
    template = loader.get_template('appointment.html')
    return HttpResponse(template.render())

def appointment2(request):
    template = loader.get_template('appointment2.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            post = login()
            user= patientaccount()
            user.name = request.POST.get('name')
            post.username = request.POST.get('email')
            user.address =request.POST.get('address')
            post.password = request.POST.get('password')
            post.role= "patient"
            post.save()
            user.save()
            return render(request, 'index.html')

        else:
            return render(request, 'index.html')

def saveappointment(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            post = Saveappointment()
            post.fullname = request.POST.get('name')
            post.addresss = request.POST.get('address')
            post.todaysdate = request.POST.get('date')
            post.dob =request.POST.get('dob')
            post.gender = request.POST.get('gender')
            post.mobile = request.POST.get('mob')
            post.doc = request.POST.get('doc')
            post.disease = request.POST.get('disease')
            post.save()
            return render(request, 'appointment2.html')

        else:
            return render(request, 'appointment2.html')

def contact(request):
    if request.method == 'POST':

        if request.POST.get('name'):

            post = contactus()
            post.name = request.POST.get('name')
            post.email = request.POST.get('email')
            post.subject = request.POST.get('subject')
            post.message = request.POST.get('message')
            post.save()

            return render(request, 'contact.html')
        else:
            return render(request, 'contact.html')

