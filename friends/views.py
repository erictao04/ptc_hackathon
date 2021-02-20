from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'GET':
        return render(request, 'friends/index.html', {'all_friends': 'all_friends'})

    if request.method == 'POST':
        if 'all_friends' in request.POST:
            return render(request, 'friends/index.html', {'all_friends': 'all_friends'})

        if 'best_friends' in request.POST:
            return render(request, 'friends/index.html', {'best_friends': 'best_friends'})

        if 'find_friends' in request.POST:
            return render(request, 'friends/index.html', {'find_friends': 'find_friends'})
