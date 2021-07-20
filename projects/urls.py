from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'profile/', views.profile, name='profile'),
    url(r'^create/', views.create, name="create"),
    url(r'^search/', views.search_results, name='search_results'),
    path('search/', views.search_results, name='search_results'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('<username>/profile/', views.profile, name='profile'),
    ]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)    