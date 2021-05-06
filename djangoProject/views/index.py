from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'gps_title': 'GPS_system'})
