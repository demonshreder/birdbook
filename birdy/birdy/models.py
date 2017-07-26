from django.db import models
from django.contrib import admin


class Bird(models.Model):
    bird_name = models.CharField(max_length=210, blank=True, null=True)
    bird_desc = models.TextField(blank=True, null=True)
    bird_location = models.CharField(max_length=210, blank=True, null=True)

    def __str__(self):
        return self.bird_name


admin.site.register(Bird)
