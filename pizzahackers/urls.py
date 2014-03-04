from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home', name='home'),
    url(r'^join$', 'core.views.join', name='join'),
    url(r'^login$', 'core.views.login', name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', 
    	{'next_page':'/'}, name='logout'),
    url(r'^about$', 'core.views.about', name='about'),
    url(r'^hacks$', 'core.views.hacks', name='hacks'),
    url(r'^rules$', 'core.views.rules', name='rules'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
