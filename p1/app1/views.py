from django.shortcuts import render
import operator
from django.http import HttpResponse
# Create your views here.
def home(requests):
    return render(requests,'app1/home.html', {'username':'YUKTHA'})
def aboutme(requests):
    return render(requests,'app1/aboutme.html',{'userid':'yukthauserid'})
def hobbies(requests):
    return render(requests,'app1/hobbies.html',{'hobbies':'watching movies,listening music,surfing net,reading books,'})
    
    
    
  

   