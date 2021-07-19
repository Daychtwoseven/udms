from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods


def indexPage(request):
    print('here')


@require_http_methods(['GET','POST'])
def loginPage(request):
    print('here')