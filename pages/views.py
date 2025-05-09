from django import views
from django.shortcuts import render

class BaseView(views.View):
    def get(request, *args, **kwargs):
        context = {

        }
        return render(request, 'base.html', context)
