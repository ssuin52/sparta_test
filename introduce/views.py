from django.shortcuts import render
from .models import AccessLog


def introduce_view(request):
    new_log = AccessLog()
    new_log.location = "index"
    new_log.save()
    return render(request, 'index.html')
