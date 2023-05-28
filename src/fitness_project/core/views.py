from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Workouts
# Create your views here.


class home_view(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home.html')



class about_view(View):
    def get(self,request,*args,**kwargs):
        return render(request,'about.html')



class warmup_view(View):
    def get(self,request,*args,**kwargs):
        return render(request,'warmup.html')

@method_decorator(login_required,name='dispatch')
class workout_list(ListView):
       template_name = 'workouts_list.html'
       queryset = Workouts.objects.all()

