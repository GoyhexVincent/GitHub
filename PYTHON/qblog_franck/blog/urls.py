from django.conf.urls import patterns, include, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),

    url(r'^format', views.BlogFormat.as_view(), name="format"),
    url(r'^format/(?P<slug>\S+)$', views.FormatDetail.as_view(), name="format_detail"),
    url(r'^feed/$', feed.LatestPostsFormat(), name="format_feed"),

    url(r'^ens', views.BlogEns.as_view(), name="ens"),
    url(r'^ens/(?P<slug>\S+)$', views.EnsDetail.as_view(), name="ens_detail"),
    url(r'^feed/$', feed.LatestPostsEns(), name="ens_feed"),

    url(r'^Admis', views.BlogAdmis.as_view(), name="Admis"),
    url(r'^Admis/(?P<slug>\S+)$', views.AdmisDetail.as_view(), name="Admis_detail"),
    url(r'^feed/$', feed.LatestPostsAdmis(), name="Admis_feed"),

    url(r'^Deb', views.BlogDeb.as_view(), name="Deb"),
    url(r'^Deb/(?P<slug>\S+)$', views.DebDetail.as_view(), name="Deb_detail"),
    url(r'^feed/$', feed.LatestPostsDeb(), name="Deb_feed"),

    url(r'^Tem', views.BlogTem.as_view(), name="Tem"),
    url(r'^Tem/(?P<slug>\S+)$', views.TemDetail.as_view(), name="Tem_detail"),
    url(r'^feed/$', feed.LatestPostsTem(), name="Tem_feed"),

    url(r'^Esp', views.BlogEsp.as_view(), name="Esp"),
    url(r'^Esp/(?P<slug>\S+)$', views.EspDetail.as_view(), name="Esp_detail"),
    url(r'^feed/$', feed.LatestPostsEsp(), name="Esp_feed"),
)