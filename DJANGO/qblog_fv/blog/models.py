from django.db import models
from django.core.urlresolvers import reverse


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




class PostgresQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Postgres(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = PostgresQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postgres_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Postgres Entry"
        verbose_name_plural = "Postgres Entries"
        ordering = ["-created"]





class BDDDQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class BDDD(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = BDDDQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("BDDD_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "BDDD Entry"
        verbose_name_plural = "BDDD Entries"
        ordering = ["-created"]



class PythonQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Python(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = PythonQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Python_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Python Entry"
        verbose_name_plural = "Python Entries"
        ordering = ["-created"]


class webQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class web(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = webQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("web_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "web Entry"
        verbose_name_plural = "web Entries"
        ordering = ["-created"]



class DiversQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Divers(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = DiversQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Divers_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "Divers Entry"
        verbose_name_plural = "Divers Entries"
        ordering = ["-created"]

class NSFWQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class NSFW(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #tags = models.ManyToManyField(Tag)

    objects = NSFWQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("NSFW_detail", kwargs={"slug": self.slug})

    class beta:
        verbose_name = "NSFW Entry"
        verbose_name_plural = "NSFW Entries"
        ordering = ["-created"]