from.import views
from django.conf.urls import url
from . import views
from django.conf.urls import include

urlpatterns = [
    url(r'^reg$', views.reg, name='reg'),
    url(r'^login$', views.login, name='login'),
    url("^soc/", include("social.apps.django_app.urls", namespace="social"))


]
