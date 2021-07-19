from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from frontend.models import CSOTable
from frontend.forms import CSOForm
# Create your views here.


@require_http_methods(['GET', 'POST'])
def csoIndexPage(request):
    try:
        form = CSOForm
        if request.method == "POST":
            pform = form(request.POST)
            if pform.is_valid():
                pform = pform.save()
                print(pform.expiry_date.year)
                print('here')
            print(pform)

        context = {
            'form': form
        }
        return render(request, 'cso/index.html', context)
    except Exception as e:
        print(e)