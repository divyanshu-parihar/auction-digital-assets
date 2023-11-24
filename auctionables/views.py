from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import NewAuctionablesForm,UpdateAuctionableForm,AuctionBiddingForm,AuctionableBids
from .models import AuctionableModel
# Create your views here.
@login_required
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


@login_required
def auction_domain(request):

    if request.method == "POST":
        new_item_form = AuctionBiddingForm(request.POST)
        if(new_item_form.is_valid()):
            instance = new_item_form.save(commit=False)
            instance.save()
            return HttpResponse('Successfully saved!')
        else:
            return HttpResponse("Form not valid")
    items = AuctionableModel.objects.all()
    
    form= AuctionBiddingForm()
    
    return render(request,'auctionables/bid_domain.html',{'items':items,"form":form})
@login_required
def me_items(request):
    items =AuctionableModel.objects.filter(item_owner=request.user)
    bids = AuctionableBids.objects.all() 
    return render(request,'auctionables/list.html',{'items':items,'bids':bids})

@login_required
def update_item(request,idx):
    item = get_object_or_404(AuctionableModel, id=idx, item_owner=request.user)
    form = UpdateAuctionableForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/items/me')  # Redirect to a page after update
    return render(request, 'auctionables/update_item.html', {'form': form, 'item': item})

@login_required
def del_item(request,idx):
    item = get_object_or_404(AuctionableModel, id=idx, item_owner=request.user)
    if request.method == 'POST':
        print("here as well")
        item.delete()
        return redirect('/items/me')
    return render(request, 'auctionables/delete_item.html', {'item': item})