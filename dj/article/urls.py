from django.conf.urls import include, patterns, url
from article import views
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('',
                       url(r'^$', views.home, name='home'),
                       url(r'^article/(?P<id>\d+)/$', views.detail, name='detail'),
                       url(r'^archives/$', views.archives, name='archives'),
                       url(r'^aboutme/$', views.aboutme, name='aboutme'),
                       url(r'^tag/(?P<tag>\w+)/$', views.tag_search, name='tag_search'),
                       url(r'^search/$', views.blog_search, name="search"),
                       url(r'^feed/$', views.RSSFeed(), name="RSS"),
                       url(r'^login/$', views.user_login, name='login'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^add_article/$', views.add_article, name='add_article'),
                       url(r'^logout/$', views.user_logout, name="logout"),
                       )
LOGIN_REDIRECT_URL = reverse_lazy('login')
