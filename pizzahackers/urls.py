from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'/?^$', 'core.views.home', name='home'),
    url(r'^join/?$', 'core.views.join', name='join'),
    url(r'^login/?$', 'core.views.login', name='login'),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', 
    	{'next_page':'/login'}, name='logout'),
    url(r'^about/?$', 'core.views.about', name='about'),
    url(r'^hacks/?$', 'core.views.hacks', name='hacks'),
    url(r'^hackers/?$', 'core.views.hackers', name='hackers'),
    url(r'^proposals/?$', 'core.views.proposals', name='proposals'),
    url(r'^proposals/(?P<action>.*)/(?P<slug>.*)/?$', 'core.views.proposals', name='proposals_edit'),
    url(r'^comment/?$', 'core.views.comment', name='comment'),
    url(r'^rules/?$', 'core.views.rules', name='rules'),
    url(r'^account/?$', 'core.views.account', name='account'),
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^(?P<username>\w+)/?$', 'core.views.profile', name='profile'),
    # url(r'^blog/', include('blog.urls')),
)
