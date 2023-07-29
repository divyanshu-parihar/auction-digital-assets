from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponse("No Auth")
    return render(request,template_name='dashboard/dashboard.html')