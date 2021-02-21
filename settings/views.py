from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'GET' or request.method == "POST" and 'account' in request.POST:
        return render(request, "settings/index.html", {"account": "account"})

    if request.method == 'POST':
        if 'password' in request.POST:
            return render(request, 'settings/index.html', {'password': 'password'})

        if 'voice_video' in request.POST:
            return render(request, 'settings/index.html', {'voice_video': 'voice_video'})

        if 'appearance' in request.POST:
            return render(request, 'settings/index.html', {'appearance': 'appearance'})
