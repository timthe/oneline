from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserProfile
from accounts.forms import UserProfileForm

def register(request):
    # http://www.djangobook.com/en/2.0/chapter14.html
    # https://www.youtube.com/watch?v=xaPHSlTmg1s&list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD&index=12
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, new_user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required(login_url='/login/')
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
        if 'picture' in request.FILES:
            profile.picture = request.FILES['picture']
            profile.save()
            return redirect('/')
    else:
        user = request.user
        profile = user.profile
        form = UserProfileForm(instance=profile)
        picture_url = None
        if UserProfile.objects.get(user=user).picture:
            picture_url = UserProfile.objects.get(user=user).picture.url
        return render(request, 'registration/profile.html', {'form': form, 'picture_url': picture_url})
