from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
from contacts.models import Contact


def register(request):
    if request.method == 'POST':
        #USER REGISTERED
        #messages.error(request, 'Testing Error Message')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check password
        #return redirect('register')
        if password == password2:
            #check user Exist in Database Or not
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This User Name is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('register')
                else:
                    #ligin after register
                    user = User.objects.create(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #auth.login(request, user)
                    #messages.success(request, 'You are now loged in')
                    User.save(self=user)
                    messages.success(request, 'You are now registered and can login ')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not  Match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        #USER LOGIN
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts':  user_contact
    }
    return render(request, 'accounts/dashboard.html', context)
