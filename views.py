from utils import render
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, "index.html")