from django.shortcuts import render,redirect
from .forms import *
from django.views.generic import TemplateView,View,ListView,FormView,CreateView,DeleteView
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from account.models import Service,charge

class Logview(FormView):
    template_name="ehome.html"
    form_class=Loginform
    def post(self,request,*args,**kwrgs):
        form_data=Loginform(data=request.POST)
        if form_data.is_valid():
            us = form_data.cleaned_data.get("username")
            pswd = form_data.cleaned_data.get("password")
            user=authenticate(request,username=us,password=pswd)
            if user:
                return redirect('custhome')
            else:
                messages.error(request,"sign in faild")
                return redirect("h")
        return render (request,"ehome.html",{"form":form_data})
    

class Regview(CreateView):
    template_name="reg.html"
    form_class=Regform
    model=User
    success_url=reverse_lazy("reg")



class Custhomeview(View):
    def get (self,request):
        return render (request,'custhome.html')
class homeview(View):
    def get (self,request):
        return render (request,'home.html')

    
class AboutHomeView(View):
    def get(self,request):
        return render(request,'about.html')
class ServiceHomeView(View):
    def get(self,request):
        return render(request,'neww.html')
    
    
class RegHomeView(View):
    def get(self,request):
        return render(request,'regg.html')
    
class ChargeHomeView(ListView):
    # def get(self,request):
    #     return render(request,'charging.html')
    template_name='charging.html'
    queryset=charge.objects.all()
    context_object_name='char'


class StationHomeView(ListView):
    # def get(self,request):
    #     return render(request,'station.html')
    template_name='station.html'
    queryset=Service.objects.all()
    context_object_name='sta'
    


class BookHomeView(View):
    def get(self,request):
        return render(request,'regg.html')
    

class paymentView(View):
    def get(self,request):
        return render(request,'payment.html')
#      
    

class HelpHomeView(View):
    def get(self,request):
        return render(request,'meet.html')
    

class Payment(TemplateView):
    template_name="payment.html"
    # def post(self,request,*args,**kwrgs):

   
class LgoutView(View):
    def get(self,request):
        logout(request)
        return redirect("home")
    

    

