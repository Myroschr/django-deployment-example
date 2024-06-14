from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

#  For login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required ## with this way we want only the user will be log in and log out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid(): ### If is new

            # Save User Form to Database
            user = user_form.save()
            print("I'm Here!!!!")
            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            # user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else: ### If is not new then display that this user is already exists
            # One of the forms was invalid if this else gets called. 
            print("I'm Here!!!!")
            print(user_form.errors,profile_form.errors) 

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'basic_app/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})



def user_login(request):
    
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        #### this method authedicate the user in one line.
        #### create an object of the user and is an authedication  way that check 
        ####the user credentials from database.
        user = authenticate(request,username = username , password = password)
        # print(user.is_authenticated)

        if user is not None:
            print("user is user")
            if user.is_active: # if the sure is active
                print("user is not active")

                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('someone tried to login and failed')
            print(f'Username: {username} and password: {password}')
            return render(request, 'basic_app/login.html',{'error_message': 'Invalid login details'})
    
    else:
        return render(request,'basic_app/login.html',{})



















            
            
            
        