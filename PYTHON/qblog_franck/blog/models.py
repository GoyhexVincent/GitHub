from django.db import models
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.contrib.gis import admin

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]




class FormatQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Format(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = FormatQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("format_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Format Entry"
        verbose_name_plural = "Format Entries"
        ordering = ["-created"]





class EnsQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Ens(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = EnsQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("ens_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Ens Entry"
        verbose_name_plural = "Ens Entries"
        ordering = ["-created"]



class AdmisQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Admis(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = AdmisQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Admis_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Admis Entry"
        verbose_name_plural = "Admis Entries"
        ordering = ["-created"]


class DebQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Deb(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = DebQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Deb_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Deb Entry"
        verbose_name_plural = "Deb Entries"
        ordering = ["-created"]



class TemQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Tem(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = TemQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Tem_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Tem Entry"
        verbose_name_plural = "Tem Entries"
        ordering = ["-created"]

class EspQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Esp(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = EspQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Esp_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Esp Entry"
        verbose_name_plural = "Esp Entries"
        ordering = ["-created"]

    class TrackRecord(models.Model):
        Nom = models.CharField("Nom de l'étudiant", max_length=50)
        Prenom = models.CharField("Prénom de l'étudiant", blank=True)
        Promotion = models.CharField("Année de la promotion", blank=True)
        Metier = models.CharField("Poste actuel", blank=True)
        date_created= models.DateTimeField(auto_now=True)
        geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.owner

    class Meta:
        verbose_name_plural = "TrackRecord"
        
admin.site.register(TrackRecord, admin.OSMGeoAdmin)