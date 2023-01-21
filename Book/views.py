from django.shortcuts import render
from Book.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn = input('Enter a topic name: ')
    T = Topic.objects.get_or_create(topic_name = tn)[0]
    T.save()
    return HttpResponse('Topic is inserted successfully!')

def insert_webpage(request):
    tn = input('Enter topic name: ')
    name = input('Enter name: ')
    url = input('Enter url: ')
    T = Topic.objects.get_or_create(topic_name = tn)[0]
    T.save()
    W = Webpage.objects.get_or_create(topic_name = T, name = name, url = url)[0]
    W.save()
    return HttpResponse('Webpage inserted succesfully!')

def insert_access(request):
    tn = input('Enter topic name: ')
    name = input('Enter name: ')
    url = input('Enter url: ')
    date = input('Enter date: ')
    T = Topic.objects.get_or_create(topic_name = tn)[0]
    T.save()
    W = Webpage.objects.get_or_create(topic_name = T, name = name, url = url)[0]
    W.save()
    A = Access_Record.objects.get_or_create(name =W, date = date)[0]
    A.save()
    return HttpResponse('Access record inserted successfully!')

