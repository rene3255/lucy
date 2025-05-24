from django.shortcuts import render


def welcome(request):
    return render(request, "applications/lucy/welcome.html")
