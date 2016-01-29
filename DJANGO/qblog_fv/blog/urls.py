from django.conf.urls import patterns, include, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^$', views.BlogIndex.as_view(), name="index"),
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),

    url(r'^postgres', views.BlogPostgres.as_view(), name="postgres"),
    url(r'^postgres/(?P<slug>\S+)$', views.PostgresDetail.as_view(), name="postgres_detail"),
    url(r'^feed/$', feed.LatestPostsPostgres(), name="postgres_feed"),

    url(r'^BDDD', views.BlogBDDD.as_view(), name="BDDD"),
    url(r'^BDDD/(?P<slug>\S+)$', views.BDDDDetail.as_view(), name="BDDD_detail"),
    url(r'^feed/$', feed.LatestPostsBDDD(), name="BDDD_feed"),

    url(r'^Python', views.BlogPython.as_view(), name="Python"),
    url(r'^Python/(?P<slug>\S+)$', views.PythonDetail.as_view(), name="Python_detail"),
    url(r'^feed/$', feed.LatestPostsPython(), name="Python_feed"),

    url(r'^web', views.Blogweb.as_view(), name="web"),
    url(r'^web/(?P<slug>\S+)$', views.webDetail.as_view(), name="web_detail"),
    url(r'^feed/$', feed.LatestPostsweb(), name="web_feed"),

    url(r'^Divers', views.BlogDivers.as_view(), name="Divers"),
    url(r'^Divers/(?P<slug>\S+)$', views.DiversDetail.as_view(), name="Divers_detail"),
    url(r'^feed/$', feed.LatestPostsDivers(), name="Divers_feed"),

    url(r'^NSFW', views.BlogNSFW.as_view(), name="NSFW"),
    url(r'^NSFW/(?P<slug>\S+)$', views.NSFWDetail.as_view(), name="NSFW_detail"),
    url(r'^feed/$', feed.LatestPostsNSFW(), name="NSFW_feed"),
)