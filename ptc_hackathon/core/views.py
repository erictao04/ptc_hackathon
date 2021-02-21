from django.shortcuts import render
from .programs import Game
# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'landing_page.html')
    elif request.method == 'POST':
        try:
            Game.launch()
        except:
            pass
        return render(request, 'landing_page.html')
