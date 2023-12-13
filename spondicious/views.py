from django.shortcuts import render

def home_view(request):
    return render(request, "spondicious/home.html", {})


def login_view(request):
    return render(request, "spondicious/login.html", {})