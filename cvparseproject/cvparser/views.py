from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, HttpResponse

# Create your views here.


class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context)

    def post(self, request):
        context = {}
        return render(request, 'home.html', context)
