from django.db import models
from django.contrib import admin


class Bird(models.Model):
    name = models.CharField(max_length=210, blank=True)
    desc = models.TextField(blank=True)
    location = models.CharField(max_length=210, blank=True)

    def __str__(self):
        return self.name


admin.site.register(Bird)
