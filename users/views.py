from django.shortcuts import render
from school_track.models import Subject, Assignment
from django.http import HttpResponseRedirect
from django.urls import reverse
from school_track.forms import SubjectForm, AssignmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()

	    return HttpResponseRedirect(reverse('home'))
    else:
	    form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})