from django.shortcuts import render


def home(request):
    Context = {
    }
    return render(
        request, 'home/index.html', Context
    )

def Service_details(request):
    Context = {
    }
    return render(
        request, 'home/service-details.html', Context
    )

