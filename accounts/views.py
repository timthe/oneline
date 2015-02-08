from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

def register(request):
    # http://www.djangobook.com/en/2.0/chapter14.html
    # https://www.youtube.com/watch?v=xaPHSlTmg1s&list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD&index=12
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
