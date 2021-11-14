from django.shortcuts import render


def home(request):
    name = "Roger"
    return render(request, 'home.html', {
        "name": name
    })
