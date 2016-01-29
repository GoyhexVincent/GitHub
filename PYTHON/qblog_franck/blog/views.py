from django.views import generic
from . import models

class BlogIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 20

class BlogDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

class BlogFormat(generic.ListView):
    queryset = models.Format.objects.published()
    template_name = "format.html"
    paginate_by = 20

class FormatDetail(generic.DetailView):
    model = models.Format
    template_name = "post.html"    


class BlogEns(generic.ListView):
    queryset = models.Ens.objects.published()
    template_name = "enseignants.html"
    paginate_by = 30

class EnsDetail(generic.DetailView):
    model = models.Ens
    template_name = "post.html"    

class BlogAdmis(generic.ListView):
    queryset = models.Admis.objects.published()
    template_name = "Admis.html"
    paginate_by = 20

class AdmisDetail(generic.DetailView):
    model = models.Admis
    template_name = "post.html"

class BlogDeb(generic.ListView):
    queryset = models.Deb.objects.published()
    template_name = "deb.html"
    paginate_by = 20

class DebDetail(generic.DetailView):
    model = models.Deb
    template_name = "post.html"

class BlogTem(generic.ListView):
    queryset = models.Tem.objects.published()
    template_name = "tem.html"
    paginate_by = 20

class TemDetail(generic.DetailView):
    model = models.Tem
    template_name = "post.html"

class BlogEsp(generic.ListView):
    queryset = models.Esp.objects.published()
    template_name = "esp.html"
    paginate_by = 20

class EspDetail(generic.DetailView):
    model = models.Esp
    template_name = "post.html"