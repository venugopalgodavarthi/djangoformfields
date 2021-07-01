from django.shortcuts import render
from registerapp.forms import RegisterF 
# Create your views here.
def registerp(request):
    form = RegisterF
    return render(request,"register.html",{'form':form})