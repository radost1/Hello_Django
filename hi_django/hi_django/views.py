from django.http import HttpResponse
from django.shortcuts import render


def about(reqvest):
    return render(reqvest,'about.html',{'gretting':'hello'})


def home(reqvest):
    return HttpResponse('This is my home')
