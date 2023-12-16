from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages


class NewTaskForm(forms.Form):
    options = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
    ]
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    image = forms.CharField(label="Image URL")
    price = forms.FloatField(label="price")
    option_field = forms.ChoiceField(choices=options, label="Choose a Category")

# Create your views here.
def index(request):
    return render(request, "homepage/index.html", {
        "form": NewTaskForm()
    })


def logout_view(request):
    logout(request)
    return redirect('index')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired home page URL
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, "homepage/login.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'home' with your desired home page URL
    else:
        form = UserCreationForm()

    return render(request, 'homepage/register.html', {'form': form})