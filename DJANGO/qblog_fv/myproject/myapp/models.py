from django.contrib.gis.db import models # Note that the models module is imported from django.contrib.gis.db  
class house4sale(models.Model):
    owner = models.CharField("Owner of the house", max_length=50)
    price = models.IntegerField("Price in $", blank=True)
    area = models.IntegerField("House area [m2]", blank=True)
    date_created= models.DateTimeField(auto_now=True)
    geom = models.PointField(srid=4326)

    def __unicode__(self):
        return self.owner

    class Meta:
        verbose_name_plural = "Houses for sale"
        
        
from django.contrib.gis import admin
admin.site.register(house4sale, admin.OSMGeoAdmin)