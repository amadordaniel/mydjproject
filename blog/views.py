from django.contrib.auth import authenticate, login, logout
from django.http import *
from django.shortcuts import render
from urlparse import urlparse

from .models import Post


def post_list(request):
    current_user = request.user
    print current_user.is_anonymous()
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts, 'current_user':current_user})


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render(request, 'blog/login.html', {})

# def logout(request, next_page=None,
#            template_name='registration/logged_out.html',
#            redirect_field_name='next',
#            current_app=None, extra_context=None):
#     """
#     Logs out the user and displays 'You are logged out' message.
#     """
#     logout(request)
#     redirect_to = request.REQUEST.get(redirect_field_name, '')
#     if redirect_to:
#         netloc = urlparse.urlparse(redirect_to)[1]
#         # Security check -- don't allow redirection to a different host.
#         return render(request, 'blog/post_list,html', {})