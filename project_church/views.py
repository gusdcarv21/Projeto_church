from django.shortcuts import render

# Create your views here.


def igreja(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')

# def login(request):
#     return render(request, 'login.html')