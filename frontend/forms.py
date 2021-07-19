from django import forms
from django.forms import ModelForm, TextInput, EmailInput, DateInput

from frontend.models import CSOTable


class CSOForm(ModelForm):
    class Meta:
        model = CSOTable
        fields = ['name', 'business_address', 'email_address', 'landline', 'fax', 'cellphone', 'contact_person',
                  'designation', 'certificate', 'dswd_certificate_accreditation_no', 'date_issued', 'expiry_date',
                  'ga', 'caap'
                  ]

        DESIGNATION_CHOICES = [
            ('President', 'President')
        ]
        CERTIFICATE_CHOICES = [
            ('Accreditation', 'Accreditation')
        ]

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'business_address': TextInput(attrs={'class': 'form-control', 'required': False}),
            'email_address': EmailInput(attrs={'placeholder': 'Please input email address', 'class': 'form-control'}),
            'landline': TextInput(attrs={'class': 'form-control'}),
            'fax': TextInput(attrs={'class': 'form-control'}),
            'cellphone': TextInput(attrs={'class': 'form-control'}),
            'contact_person': TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(choices=DESIGNATION_CHOICES, attrs={'class': 'form-control'}),
            'certificate': forms.Select(choices=CERTIFICATE_CHOICES, attrs={'class': 'form-control'}),
            'dswd_certificate_accreditation_no': TextInput(attrs={'class': 'form-control'}),
            'date_issued': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiry_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ga': TextInput(attrs={'class': 'form-control'}),
            'caap': TextInput(attrs={'class': 'form-control'}),

        }

        labels = {
            'dswd_certificate_accreditation_no': 'DSWD Certificate Accreditation No'
        }
