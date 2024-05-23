from django.shortcuts import render, redirect

from myapp1.models import Worker
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from .match_prediction import match, visualize_statistics, get_match_statistics
from .stats import *


def index(request):
    tours = tournaments()
    teams = get_most_successful_teams()
    return render(request, 'index.html', {"tournaments": tours, "teams": teams})


# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def match_prediction_view(request):
    prediction = None
    plot_filename = None
    stats = None
    if request.method == 'POST':
        home_team = request.POST.get('home_team')
        away_team = request.POST.get('away_team')
        stats = get_match_statistics(home_team, away_team)
        plot_filename = visualize_statistics(home_team, away_team)
        prediction = match(home_team, away_team)
        print(stats)
    return render(request, 'match_prediction.html', {'prediction': prediction, 'plot': plot_filename, 'stats': stats})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')
