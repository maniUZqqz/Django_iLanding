from django.shortcuts import render


def home(request):
    Context = {
    }
    return render(
        request, 'home/index.html', Context
    )


