"""iitbapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import gcm.urls

import authentication.urls
import news.urls
import event.urls
import notice.urls
import information.urls
import content.urls
import core.urls
import feed.urls
import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^public/', include(information.urls)),
    url(r'^content/', include(content.urls)),
    url(r'^logs/', views.logs),
    url(r'^$', views.index, name='index_page'),
    url(r'^about/', views.about, name='about_page'),
    url(r'', include(authentication.urls)),
    url(r'', include(news.urls)),
    url(r'', include(event.urls)),
    url(r'', include(notice.urls)),
    url(r'', include(gcm.urls)),
    url(r'', include(core.urls)),
    url(r'', include(feed.urls)),
]

urlpatterns += [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
]
