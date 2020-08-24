from django.shortcuts import render
from django.http import HttpResponse
import operator 
def home(requests):
    return render(requests,'revcon/home.html')
def output(requests):
    text1=requests.GET['string1']
    text2=requests.GET['string2']
    text1=text1[::-1]
    text2=text2[::-1]
    result=text1+text2
    return render(requests,'revcon/output.html',{'res':result})

  