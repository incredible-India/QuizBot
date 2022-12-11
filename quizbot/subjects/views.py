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
        
        if 'q1' in request.session:
            q1 = request.session['q1']
        else:
            q1 = ''
        if 'q2' in request.session:
            q2 = request.session['q2']
        else:
            q2 = ''
        if 'q3' in request.session:
            q3 = request.session['q3']
        else:
            q3 = ''
        if 'q4' in request.session:
            q4 = request.session['q4']
        else:
            q4 = ''

  
        data = Misc.objects.all()
        return render(request, 'subjects/misc.html',{
        'data':data,
        'number' : len(data),
        'question' : question,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4
        })
    def post(self, request):
        question = request.POST.get('question')
        q1=request.POST.get('q1')
        q2=request.POST.get('q2')
        q3=request.POST.get('q3')
        q4=request.POST.get('q4')

        #validation of question to be inserted 

        if len(question.strip()) <= 5:
             messages.error(request,'Question Cannot be blank or less than 5 characters..')

             request.session['question'] = question
             request.session['q1'] = q1
             request.session['q2'] = q2
             request.session['q3'] = q3
             request.session['q4'] = q4

             return HttpResponseRedirect('/settings')
            
        elif len(q1.strip())<=0 or len(q2.strip()) <=0 or len(q3.strip()) <= 0 or len(q4.strip()) <= 0:
            messages.error(request,'Option cannot be blank')
            request.session['question'] = question
            

          
            request.session['q1'] = q1
            request.session['q2'] = q2
            request.session['q3'] = q3
            request.session['q4'] = q4
            return HttpResponseRedirect('/settings')
        
        if 'question' in request.session:

            del request.session['question']
        if 'q1' in request.session:
            del request.session['q1']
        if 'q2' in request.session:
            del request.session['q2']
        if 'q3' in request.session:
            del request.session['q3']
        if 'q4' in request.session:
            del request.session['q4']


        
        Misc.objects.create(question=question,op1=q1,op2=q2,op3=q3,op4=q4).save()

        messages.info(request,'Question Added Successfully')
        return HttpResponseRedirect('/settings')






#for deleting the question of Misc .objects.

class deleteQuestion(View):
    def get(self, request,data):

        isExist = Misc.objects.filter(slug=data)


        if isExist.exists():
            isExist.delete()
            messages.success(request,"Question Deleted Successfully")
            return HttpResponseRedirect('/settings')

        else:
            return HttpResponse("<h1> Something Went Wrong...Err101")




#edit misc question     

class EditQuestion(View):
    def get(self, request,data):

        isExist = Misc.objects.filter(slug=data)

        if isExist.exists():
            ques = Misc.objects.get(slug=data)
            return render(request, 'subjects/editmsc.html',{'data':isExist,'ques':ques})
        else:
            return HttpResponse('Something Went Wrong !!!! Err102')