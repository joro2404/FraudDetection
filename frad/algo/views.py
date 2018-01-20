from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import messages

def index(request):
    data = request.GET.get('q','')
    print(data)

    # model.predict(data)

    return HttpResponse(request)
    messages.add_message(request, messages.INFO, data)
