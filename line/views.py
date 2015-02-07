from django.shortcuts import render, redirect
from line.models import Item
from line.forms import ItemForm
from django.contrib.auth.decorators import login_required

def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})

@login_required(login_url='/login/')
def new_line(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return render(request, 'newline.html', {'form':form})