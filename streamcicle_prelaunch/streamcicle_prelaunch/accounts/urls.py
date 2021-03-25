
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

# Current pages under the scope of accounts

urlpatterns = [
    path('', views.signup, name='signup' )]