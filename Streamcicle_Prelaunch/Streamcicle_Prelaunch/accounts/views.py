import time
import os
from django.views.generic import View
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from Streamcicle_Prelaunch.settings import EMAIL_HOST_USER
from django.db import connection
from . import forms
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from .models import StreamcicleSubscribers
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template.loader import render_to_string
from email.mime.image import MIMEImage
from django.db import connection
from django.http import HttpResponseRedirect
# Create your views here.
#DataFlair #Send Email
def get_query():
    print(StreamcicleSubscribers.objects.all().values())

def error(request):
    template = get_template('error.html')
    return render(request,'error.html' )

def signup(request):
    
    try:
        if request.method == 'POST':
            form = forms.CustomUserCreationForm(request.POST)
            email = request.POST['email']
            first_name = request.POST['first_name']
            if form.is_valid():
                user_new = form.save(commit=False)
                user_new.username = email
                user_new.SubscriberFirstName = first_name
                user_new.SubscriberEmail = email
                user_new.email= email
                user_new.SubscriberType = "G"
                user_new.save()
                get_query()
            else:
                print(form.errors)
            current_site = get_current_site(request)
            print(current_site)
            template = get_template('success.html')
            context = {
                    'domain': current_site.domain,
                    }
            subject = 'Something new is coming to Streamcicle!'
            message = template.render(context)
            to_email = str(email)
            to_email = form.cleaned_data.get('email')
            email = EmailMultiAlternatives(
                            subject, message, to=[to_email], bcc=['mary.s1368@gmail.com'])
            email.content_subtype = "html"
            email.mixed_subtype = 'related'
            img_path = './static/Resource/template_img.png'
            with open(img_path, 'rb') as img:
                image = MIMEImage(img.read())
                email.attach(image)
                image.add_header('Content-ID', "<{}>".format('template_img.png'))
            email.send()
            print('email_Send')
            return  render(request, 'EmailRegister.html', {'form':form}) #redirect('/#/')
        else:
            form = CustomUserCreationForm()
            return render(request, 'EmailForm.html', {'form':form})
    except:
        return redirect('error')
        
# Create your views here.
def home(request):
    return render(request,"EmailForm.html",{})




    
