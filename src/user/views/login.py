from django.shortcuts import render
from ..forms.user import NewUserForm, UserProfileInfoForm, LoginForm

from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'user/index.html')
    
def user_login(request):
    print(request.POST)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return HttpResponse('Account not active')
            else:
                print(f'Invalid login details: Username: {username} and Password: {password}')
                return HttpResponse('Invalid login details supplied!')

    return render(request, 'user/login.html', {'form': LoginForm()})

@login_required    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_resgistration(request):

    registered = False

    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        profile_form = UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            if 'portfolio_site' in request.POST:
                profile.portfolio_site = request.POST['portfolio_site']
            
            profile.save()

            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)
        
    return render(request, 'user/registration.html', {'user_form': NewUserForm(), 'profile_form': UserProfileInfoForm(), 'registered': registered})