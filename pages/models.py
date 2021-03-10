import os
from django.db import models
from django.shortcuts import reverse
from django.core.exceptions import ValidationError

from tinymce.models import HTMLField


# Create your models here.
class OralHistoriesPage(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cold War Oral Histories Page"
        verbose_name_plural = "Cold War Oral Histories Page"


class DynamicFlightSimulatorPage(models.Model):
    title = models.CharField(max_length=100)
    blueprint = HTMLField(
        verbose_name="Blueprint Digitization Project", blank=True, null=True
    )
    centrifuge = HTMLField(
        verbose_name="Centrifuge Logbook Digitization", blank=True, null=True
    )
    tours = HTMLField(verbose_name="Tours of The Fuge", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Dynamic Flight Simulator Page"
        verbose_name_plural = "Dynamic Flight Simulator Page"


class NADCPhotoPage(models.Model):
    title = models.CharField(max_length=100)
    description = HTMLField(verbose_name="Page Text")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "NADC Photo Page"
        verbose_name_plural = "NADC Photo Page"


def nadc_uploads(instance, filename):
    upload_path = "nadc_images"
    return os.path.join(upload_path, filename.lower())


class NADCPhoto(models.Model):
    photo = models.ImageField(upload_to=nadc_uploads)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "NADC Photo"
        verbose_name_plural = "NADC Photos"

    def get_comments(self):
        comments = NADCPhotoComment.objects.filter(
            photo=self.id, approved=True)
        return comments

    def comment_count(self):
        count = NADCPhotoComment.objects.filter(
            photo=self.id, approved=True).count()
        return count


class NADCPhotoComment(models.Model):
    photo = models.ForeignKey(NADCPhoto, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.photo.id, self.name, self.date)

    class Meta:
        ordering = ["-date"]
        verbose_name = "NADC Photo Comment"
        verbose_name_plural = "NADC Photo Comments"


EVENT_CATEGORIES = [
    ("HIOB", "History In Our Backyard"),
    ("MOVIE", "Movie Night"),
    ("AVT", "Annual Veterans Tribute"),
    ("OTHER", "Other Activites"),
]


def event_uploads(instance, filename):
    upload_path = "event_images"
    return os.path.join(upload_path, filename.lower())


class Event(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=5, choices=EVENT_CATEGORIES, default="HIOB")
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=False, auto_now=False)
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = HTMLField()
    header_img = models.ImageField(
        upload_to=event_uploads, blank=True, null=True)
    event_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})


class EventPhoto(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=event_uploads)

    def __str__(self):
        return self.event.title + "-" + str(self.id)


class EventDescriptions(models.Model):
    hiob = HTMLField(verbose_name="History In Our Backyard")
    movie = HTMLField(verbose_name="Movie Nights")
    avt = HTMLField(verbose_name="Annual Veterans Tribute")

    def __str__(self):
        return "Event Category Descriptions"

    class Meta:
        verbose_name = "Event Category Descriptions"
        verbose_name_plural = "Event Category Descriptions"
