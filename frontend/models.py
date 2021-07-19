# Create your models here.
from django.db import models


class CSOTable(models.Model):
    DESIGNATION_CHOICES = [
        ('President', 'President')
    ]
    CERTIFICATE_CHOICES = [
        ('Accreditation', 'Accreditation')
    ]
    name = models.CharField(max_length=100)
    business_address = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField(max_length=100, null=True, blank=True)
    landline = models.CharField(max_length=15, null=True, blank=True)
    fax = models.CharField(max_length=20, null=True, blank=True)
    cellphone = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=15)
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    certificate = models.CharField(max_length=20, choices=CERTIFICATE_CHOICES)
    dswd_certificate_accreditation_no = models.CharField(max_length=100)
    date_issued = models.DateField()
    expiry_date = models.DateField()
    ga = models.CharField(max_length=10)
    caap = models.CharField(max_length=100)
