from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("No Auth")
    return HttpResponse("<h1>Hello World</h1>")


