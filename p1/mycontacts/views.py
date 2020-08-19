from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import operator

def names(requests):
    return HttpResponse('home,family,friends,work')
def numbers(requests):
    return HttpResponse('Indian number has 10 digits and begins with +91')



