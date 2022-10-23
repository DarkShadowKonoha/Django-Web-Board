from django.urls import re_path
from django.contrib import admin

from accounts import views as accounts_views
from boards import views


urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    re_path(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    re_path(r'^admin/', admin.site.urls),
]