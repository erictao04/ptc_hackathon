from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'landing_page.html')
    elif request.method == 'POST':
        try:
            from .programs import Game
            Game.launch()
        except:
            pass
        return render(request, 'landing_page.html')
