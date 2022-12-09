from django.shortcuts import render,HttpResponse
from .models import Misc
from django.views import View
# Create your views here.

class adminPage(View):

    def get(self, request):

  
        data = Misc.objects.all()
        return render(request, 'subjects/misc.html',{
        'data':data,
        'number' : len(data),
        })
    def post(self, request):
        question = request.POST.get('question')
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')

        return HttpResponse(question)