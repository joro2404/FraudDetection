from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    param = request.GET.get('q', '')
    print(param)
    return HttpResponse(request)
