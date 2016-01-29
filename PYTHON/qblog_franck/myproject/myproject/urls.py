from django.conf.urls import patterns, include, url

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add_point/$', 'myapp.views.add_point'),
    url(r'^add_point/error$', 'myapp.views.form_error'),
    url(r'^add_point/success$', 'myapp.views.form_success'),
)