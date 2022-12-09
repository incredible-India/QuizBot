from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Misc
from django.views import View
from django.contrib import messages
# Create your views here.

class adminPage(View):

    def get(self, request):


        if 'question' in request.session:
            question = request.session['question']
        else:
            question = ''

  
        data = Misc.objects.all()
        return render(request, 'subjects/misc.html',{
        'data':data,
        'number' : len(data),
        'question' : question
        })
    def post(self, request):
        question = request.POST.get('question')
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')

        #validation of question to be inserted 

        if len(question.strip()) <= 5:
             messages.info(request,'Question Cannot be blank or less than 5 characters..')

             request.session['question'] = question

             return HttpResponseRedirect('/settings')
            
        elif len(q1.strip())<=0 or len(q2.strip()) <=0 or len(q3.strip()) <= 0 or len(q4.strip()) <= 0:
            messages.info(request,'Option cannot be blank')
            request.session['question'] = question
            return HttpResponseRedirect('/settings')
        
        return HttpResponse(question)
             