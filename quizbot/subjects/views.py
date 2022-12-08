from django.shortcuts import render
from .models import Misc
# Create your views here.
def adminPage(request):

    data = Misc.objects.all()
    return render(request, 'subjects/misc.html',{
        'data':data,
        'number' : len(data),
    })