from django.shortcuts import render
from .models import Edition

def index(request):
    editions = Edition.objects.all()
    return render(request, 'library/index.html', {'editions': editions})