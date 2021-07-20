from django.http.response import HttpResponseRedirect
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
import random
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.order_by('-votes_total')
    # # rates = RateModel.objects.order_by('user')
    # # avg = RateModel.objects.aggregate(design = Avg('design'), usability = Avg('usability'), content = Avg('content'))
    # # dict = {'records': posts, 'rates': rates, 'avg': avg}
    # ratings = Rating.objects.filter(user=request.user, post=post).first()
    # rating_status = None
    # if ratings is None:
    #     rating_status = False
    # else:
    #     rating_status = True
    # if request.method == 'POST':
    #     form = RatingsForm(request.POST)
    #     if form.is_valid():
    #         rate = form.save(commit=False)
    #         rate.user = request.user
    #         rate.post = post
    #         rate.save()
    #         post_ratings = Rating.objects.filter(post=post)

    #         design_ratings = [d.design for d in post_ratings]
    #         design_average = sum(design_ratings) / len(design_ratings)

    #         usability_ratings = [us.usability for us in post_ratings]
    #         usability_average = sum(usability_ratings) / len(usability_ratings)

    #         content_ratings = [content.content for content in post_ratings]
    #         content_average = sum(content_ratings) / len(content_ratings)

    #         score = (design_average + usability_average + content_average) / 3
    #         print(score)
    #         rate.design_average = round(design_average, 2)
    #         rate.usability_average = round(usability_average, 2)
    #         rate.content_average = round(content_average, 2)
    #         rate.score = round(score, 2)
    #         rate.save()
    #         return HttpResponseRedirect(request.path_info)
    # else:
    #     form = RatingsForm()
    # params = {
    #     'post': post,
    #     'rating_form': form,
    #     'rating_status': rating_status

    # }
    return render(request, 'index.html', {'posts':posts,})#context=dict

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



def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'posts/search.html',{"message":message,"articles": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'posts/search.html',{"message":message})           