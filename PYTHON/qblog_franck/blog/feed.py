from django.contrib.syndication.views import Feed
from .models import Entry, Format, Ens, Admis, Deb, Tem


class LatestPosts(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Entry.objects.published()[:5]

class LatestPostsFormat(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Format.objects.published()[:5]
       
class LatestPostsEns(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Ens.objects.published()[:5]

class LatestPostsAdmis(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Admis.objects.published()[:5]

class LatestPostsDeb(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Deb.objects.published()[:5]

class LatestPostsTem(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Tem.objects.published()[:5]

class LatestPostsEsp(Feed):
    title = "Q Blog"
    link = "/feed/"
    description = "Latest Posts of Q"

    def items(self):
        return Esp.objects.published()[:5]