from sys import path
from django.conf.urls import url
from.import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^aboutus/', views.aboutus),
    url(r'^ayurveda/', views.ayurveda),
    url(r'^contact/', views.contact),
    url(r'^departments/', views.departments),
    url(r'^doctors/', views.doctors),
    url(r'^appointment/', views.appointment,name="before login"),
    url(r'^appointment2/', views.appointment2,name="after login"),
    url(r'^signup/', views.signup),
    url(r'^saveappointment', views.saveappointment),
    url(r'^contactus', views.contact),
]