from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.http import Http404, JsonResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Decorative,Care

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

class PollsView(generic.ListView):
    template_name = 'makeup/polls.html'
    context_object_name = 'types_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Decorative.objects.all()

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



