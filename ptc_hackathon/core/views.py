from django.shortcuts import render
from .programs import Game
# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'landing_page.html')
    elif request.method == 'POST':
        Game.launch()
        return render(request, 'landing_page.html')
