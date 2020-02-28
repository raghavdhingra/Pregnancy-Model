from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "Pregnancy Model"
    }
    return render(request,"home.html",context)

def pregnancyApi(request):
    context = {

    }
    return render(request,"index.html",context)