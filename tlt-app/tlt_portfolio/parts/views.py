from django.shortcuts import render

from .models import Parts


def index(request):
    projects = Parts.objects.all()
    return render(request, 'parts/index.html', {'projects': projects})
