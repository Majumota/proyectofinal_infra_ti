from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"core/index.html")

def juli(request):
    return render(request,"core/juli.html")

def pablo(request):
    return render(request,"core/pablo.html")
