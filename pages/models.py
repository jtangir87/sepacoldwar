import os
from django.db import models
from django.shortcuts import reverse

from tinymce.models import HTMLField


def event_uploads(instance, filename):
    upload_path = "event_images"
    return os.path.join(upload_path, filename.lower())


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    date = models.DateField(auto_now_add=False, auto_now=False)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = HTMLField()
    header_img = models.ImageField(upload_to=event_uploads, blank=True, null=True)
    event_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("blog:blog_detail", kwargs={"slug": self.slug})