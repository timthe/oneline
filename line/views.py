from django.shortcuts import render, redirect
from line.models import Item
from line.forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    # http://www.djangobook.com/en/2.0/chapter14.html
    # https://www.youtube.com/watch?v=xaPHSlTmg1s&list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD&index=12
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
