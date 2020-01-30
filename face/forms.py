from django import forms
from .models import Registration

class RegistrationForm(forms.Form):
    class Meta:
        model = Registration
        #fields = ['image', 'image']


    name=forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )
    
    email=forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email Id'
            }
        )
    )
    mobile=forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'MobileNumber'
            }
        )
    )

    image = forms.ImageField()



class CheckForm(forms.Form):
    image = forms.ImageField()
