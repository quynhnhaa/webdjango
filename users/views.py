from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class ViewIndex(View):
    def get(self, request):
        return HttpResponse("HELOO")