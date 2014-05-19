from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from forms import UserCreationForm, UserProfileForm, ImageUploadForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = auth.authenticate(username=request.POST['username'], 
                                    password=request.POST['password2'])
            if user is not None and user.is_active:
                auth.login(request, user)
            return HttpResponseRedirect("../")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {'form': form,})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

    else:
        form = UserProfileForm(instance=request.user)
    return render(request, "accounts/profile.html", {
        'form': form, 
        })

@login_required
def avatar(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES) 
        if form.is_valid():
            request.user.avatar = form.cleaned_data['image']   
            request.user.save()
    
    return HttpResponseRedirect("../profile/")

