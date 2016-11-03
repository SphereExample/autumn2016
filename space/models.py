from __future__ import unicode_literals

from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    star_system = models.ForeignKey(to='StarSystem', blank=True, null=True)

    def __unicode__(self):
        return self.name
    

class Star(models.Model):
    name = models.CharField(max_length=255)
    star_system = models.ForeignKey('StarSystem')

    def __unicode__(self):
        return self.name


class StarSystem(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name
