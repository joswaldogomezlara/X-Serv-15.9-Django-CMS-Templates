from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms_templates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^annotated/(.+)$', 'contentApp.views.templates_handler'),
    url(r'^(.*)$', 'contentApp.views.pages_handler'),
)
