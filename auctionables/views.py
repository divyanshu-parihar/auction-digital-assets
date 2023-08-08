from django.shortcuts import render,HttpResponse
from .forms import NewAuctionablesForm
from .models import AuctionableModel
# Create your views here.
def new_item(request):
    if request.method == "POST":
        new_item_form = NewAuctionablesForm(request.POST)
        new_item_form.item_owner = request.user
        if(new_item_form.is_valid()):
            instance = new_item_form.save(commit=False)
            instance.item_owner = request.user 
            instance.save()
            return HttpResponse('Successfully saved!')
        else:
            return HttpResponse("Form not valid")
    new_item_form = NewAuctionablesForm()
    return render(request,'auctionables/new.html',{"form":new_item_form})

def me_items(request):
    items =AuctionableModel.objects.filter(item_owner=request.user)
    return render(request,'auctionables/list.html',{'items':items})