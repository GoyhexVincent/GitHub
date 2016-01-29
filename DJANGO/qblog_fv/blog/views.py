from django.views import generic
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 20

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class BlogPostgres(generic.ListView):
    queryset = models.Postgres.objects.published()
    template_name = "postgres.html"
    paginate_by = 20

class PostgresDetail(generic.DetailView):
    model = models.Postgres
    template_name = "post.html"    


class BlogBDDD(generic.ListView):
    queryset = models.BDDD.objects.published()
    template_name = "BDDD.html"
    paginate_by = 30

class BDDDDetail(generic.DetailView):
    model = models.BDDD
    template_name = "post.html"    

class BlogPython(generic.ListView):
    queryset = models.Python.objects.published()
    template_name = "Python.html"
    paginate_by = 20

class PythonDetail(generic.DetailView):
    model = models.Python
    template_name = "post.html"

class Blogweb(generic.ListView):
    queryset = models.web.objects.published()
    template_name = "web.html"
    paginate_by = 20

class webDetail(generic.DetailView):
    model = models.web
    template_name = "post.html"

class BlogDivers(generic.ListView):
    queryset = models.Divers.objects.published()
    template_name = "Divers.html"
    paginate_by = 20

class DiversDetail(generic.DetailView):
    model = models.Divers
    template_name = "post.html"

class BlogNSFW(generic.ListView):
    queryset = models.NSFW.objects.published()
    template_name = "NSFW.html"
    paginate_by = 20

class NSFWDetail(generic.DetailView):
    model = models.NSFW
    template_name = "post.html"