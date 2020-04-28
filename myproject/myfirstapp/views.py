"""My views"""
from django.shortcuts import render

# render index.html without context
def index(request):
    return render(request, 'index.html')

