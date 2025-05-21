

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required
def formulariov(request):
    return render(request, 'formulariosv.html')