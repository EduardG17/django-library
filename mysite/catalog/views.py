from django.shortcuts import render
from .models import Edition

def index(request):
    editions = Edition.objects.all()
    return render(request, 'catalog/index.html', {'editions': editions})