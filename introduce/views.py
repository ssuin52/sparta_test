from django.shortcuts import render
from .models import AccessLog


def introduce_view(request):
    if request.method == 'POST':
        create_at = request.POST.get('create_at',None)
        location = request.POST.get('location',None)

        new_log = AccessLog()
        new_log.created_at = create_at
        new_log.location = location
        new_log.save()
        
    elif request.method == 'GET':
        return render(request, 'index.html')
