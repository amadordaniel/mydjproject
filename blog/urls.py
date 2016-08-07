from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^management/logout/$', 'django.contrib.auth.views.logout'),
]
