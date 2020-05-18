from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    error_css_class = ''
    required_css_class = ''

    username = forms.CharField(label="Username")
    username.widget.attrs.update({'class' : 'form-control'})

    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password.widget.attrs.update({'class' : 'form-control'})

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password.widget.attrs.update({'class' : 'form-control'})
    password2 = forms.CharField(label="Repeat Password",widget=forms.PasswordInput)
    password2.widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = User
        fields = ('username','first_name','email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password Doesnt Match')
        return cd['password2']
