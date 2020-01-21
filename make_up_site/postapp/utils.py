from django.shortcuts import render,redirect
from .models import *

class ObjectCreateMixin:

    form_model=None
    template=None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, context={'form':form})

    def post(self,request):
        bound_form=self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj=bound_form.save()
            return redirect(new_obj)
        return render(request, self.template,context={'form':bound_form})
