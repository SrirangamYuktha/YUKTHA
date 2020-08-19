from django.shortcuts import render
import operator
from django.http import HttpResponse
# Create your views here.
def home(requests):
    return HttpResponse('<h1>This is home page</h1>')
def aboutme(requests):
    return HttpResponse('I am Srirangam Yuktha')
def hobbies(requests):
    return HttpResponse('HOBBIES: watching movies,listening music,surfing net,reading books')