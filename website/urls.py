from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.blog.views.home', name='home'),
    url(r'project/(?P<project>[\w|\W]+)/$', 'website.blog.views.project', name='project'),

    url(r'^admin/', include(admin.site.urls)),
)
