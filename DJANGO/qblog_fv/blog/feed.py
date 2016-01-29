from django.contrib.syndication.views import Feed
from .models import Entry, Postgres, BDDD, Python, web, Divers


class LatestPosts(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Entry.objects.published()[:5]

class LatestPostsPostgres(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Postgres.objects.published()[:5]
       
class LatestPostsBDDD(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return BDDD.objects.published()[:5]

class LatestPostsPython(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Python.objects.published()[:5]

class LatestPostsweb(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return web.objects.published()[:5]

class LatestPostsDivers(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Divers.objects.published()[:5]

class LatestPostsNSFW(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return NSFW.objects.published()[:5]