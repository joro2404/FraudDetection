from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import messages
def index(request):
    parm=request.GET.get('q','')
    print(parm)
    return HttpResponse(request)
    messages.add_message(request, messages.INFO, parm)
