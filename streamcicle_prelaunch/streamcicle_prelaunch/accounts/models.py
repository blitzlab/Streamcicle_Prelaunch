from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

# Create your models here.
class StreamcicleSubscribers(AbstractUser):
    SubscriberFirstName = models.CharField( max_length=30, blank=False, null=True)
    SubscriberEmail = models.EmailField( blank=False, null = False)
    SubscriberType = models.CharField( max_length=30, blank=False, null=True)
    # # # # password = 'none'
    # last_login = 'none'
    # # is_superuser ='none'
    # # last_name = 'none'
    # # first_name = 'none'
    # # email = 'none'
    # # is_staff = 'none'
    first_name = models.CharField( max_length=30, blank=False, null=True)
    email = models.EmailField( blank=False, null = False)
    
    