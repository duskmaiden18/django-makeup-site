from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views import generic
from django.http import Http404, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View


from .models import Decorative,Care,FavCare
from .forms import CareForm

# Create your views here.

def index(request):
    return render(request, 'makeup/index.html')

def types(request):
    return render(request, 'makeup/types.html')

class DecorView(generic.ListView):
    template_name = 'makeup/decor.html'
    context_object_name = 'decor_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Decorative.objects.all()

class CareView(generic.ListView):
    template_name = 'makeup/care.html'
    context_object_name = 'care_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Care.objects.all()


def polls(request):
    return render(request, 'makeup/polls.html')

class DecorPollsView(generic.ListView):
    template_name = 'makeup/decor_polls.html'
    context_object_name = 'types_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Decorative.objects.all()

class CarePollsView(View):

    def get(self,request):
        form = CareForm()
        return render(request, 'makeup/care_polls.html',context={'form':form})

    def post(self,request):
        choice_id=request.POST['companies']
        selected_choice=FavCare.objects.get(pk=choice_id)
        selected_choice.votes+=1
        selected_choice.save()
        results=FavCare.objects.all()
        return render(request,'makeup/care_results.html',context={'results':results})
        # bound_form = CareForm(request.POST)
        # if bound_form.is_valid():


@csrf_exempt
def dbchange(request):
    print("qwerty")
    mass1=[]
    mass2=[]
    mass3=[]
    choice_id=request.POST.get('choice_id')
    question_id=request.POST.get('question_num')
    print(choice_id)
    d=Decorative.objects.get(pk=question_id)
    all_choice=d.fav_set.all()
    selected_choice=d.fav_set.get(pk=choice_id)
    selected_choice.votes+=1
    selected_choice.save()
    for i in all_choice:
        mass1.append(i.choice_text)
        mass2.append(i.votes)
        mass3.append(i.id)
    context={"id":mass3,"votes":mass2,"choice":mass1}
    return JsonResponse(context)



