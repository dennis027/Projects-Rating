from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import utc
from django.db.models import Avg 

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.order_by('-votes_total')
    rates = RateModel.objects.order_by('user')
    avg = RateModel.objects.aggregate(design = Avg('design'), usability = Avg('usability'), content = Avg('content'))
    dict = {'records': posts, 'rates': rates, 'avg': avg}
    return render(request, 'index.html', {'posts':posts})

@login_required(login_url='/accounts/login/') 
def profile(request):
    

    posts = Post.objects.order_by('-votes_total')
    return render(request, 'index.html', {'posts':posts})




def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():        
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 


@login_required
# def create(request):
#     if request.method == 'POST':
#         if request.POST['title']  and request.POST['url']:
#             post = Post()
#             post.title = request.POST['title']
#             if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
#                 post.url = request.POST['url']
#             else:
#                 post.url = 'http://' + request.POST['url']
#             post.pub_date = datetime.datetime.utcnow().replace(tzinfo=utc)
#             post.author = request.user
#             post.save()
#             return redirect('index')
#         else:
#             return render(request, 'posts/create_post.html', {'error': 'Error: You need a title and URL to post!'})
#     else:
#         return render(request, 'posts/create_post.html')    

def create(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'posts/create_post.html', {"form": form})            