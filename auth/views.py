from django.shortcuts import render,redirect
from .forms import SignUpForm, LoginForm
# Create your views here
def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/auth/login/')
        else:
            return render(request,'auth/signup.html',{
            'form':form,
    }) 
    form = SignUpForm()
    return render(request,'auth/signup.html',{
        'form':form
    })

# def login(request):
#     form = LoginForm()
#     return render(request,'auth/login.html',{
#         'form':form
#     })