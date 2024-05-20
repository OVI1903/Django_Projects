from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def control(request):
    data = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'members': data,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    tomb = Member.objects.get(id=id)
    template1 = loader.get_template('details.html')
    context1 = {
    'defers': tomb,
    }

    return HttpResponse(template1.render(context1, request))

def main(request):
    template3 = loader.get_template('main.html')
    return HttpResponse(template3.render())