from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib import messages
from .ml_model.model import Model

def index(request):
    data = request.GET.get('q','')
    # print(data)

    model = Model()
    resp = model.predict(data)

    return HttpResponse(resp)
    messages.add_message(request, messages.INFO, data)
