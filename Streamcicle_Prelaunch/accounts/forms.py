from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import UserCreationForm
from .models import StreamcicleSubscribers as User

from django.utils.translation import ugettext, ugettext_lazy as _
#forms.ModelForm
#Form for creating new user
class CustomUserCreationForm(UserCreationForm):
    password1 = \
        forms.CharField(label=_(""),widget=forms.PasswordInput(attrs={'placeholder':'Password'}), 
                        required = False)
    password2 = \
        forms.CharField(label=_(""),widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),
                        required = False)
    username = forms.CharField(required = False)
    class Meta():
        model = User
        fields = ('username','first_name', 'email', 'password1', 'password2')
        help_texts = {
            'username' : ''
        }

        labels = {
            'username' : '',    
        }
        #Include placeholder text
        widgets = {
            'first_name' :forms.TextInput(attrs= {'placeholder':'First name'}),
            'email' :forms.TextInput(attrs= {'placeholder':'Email'}), 
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.errors['email'] = ['Email already exists']
        return self.cleaned_data

    def clean_email(self):
        """
        ensure that email is always lower case.
        """
        return self.cleaned_data['email'].lower()