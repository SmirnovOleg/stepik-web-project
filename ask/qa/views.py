from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello!', status=200)


def question(request, *args, **kwargs):
    content = str(args) + str(kwargs)
    return HttpResponse(content, status=200)
