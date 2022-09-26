from django.shortcuts import render

def introduce_view(request):
    return render(request, 'index.html')
