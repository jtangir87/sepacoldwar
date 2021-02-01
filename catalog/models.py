import os
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Collection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Collection"
        verbose_name_plural = "Collections"


class FileType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "File Type"
        verbose_name_plural = "File Types"


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Keyword"
        verbose_name_plural = "Keywords"


def catalog_files(instance, filename):
    upload_path = "catalog_files"
    return os.path.join(upload_path, filename.lower())


class CatalogItem(models.Model):
    accession_number = models.CharField(
        max_length=25, blank=True, null=True, verbose_name="Accession Number")
    accession_date = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True, verbose_name="Accession Date")
    obj_name = models.CharField(
        max_length=250, blank=True, null=True, verbose_name="Object Name")
    obj_file = models.FileField(
        upload_to=catalog_files, blank=True, null=True, verbose_name="Object")
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name="categories")
    collection = models.ManyToManyField(Collection, related_name="collections")
    source_name = models.CharField(max_length=250, blank=True, null=True)
    source_url = models.URLField(blank=True, null=True)
    approx_obj_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name="Approximate Object Date")
    start_year = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="Start Year Range")
    end_year = models.PositiveIntegerField(
        blank=True, null=True, verbose_name="End Year Range")
    added_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Added By")
    file_format = models.ForeignKey(
        FileType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="File Type")
    provenance = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    accession_img = models.ImageField(
        upload_to=catalog_files, blank=True, null=True, verbose_name="Accession Image")
    accession_img_caption = models.TextField(
        blank=True, null=True, verbose_name="Accession Image Caption")
    accession_img_description = models.TextField(
        blank=True, null=True, verbose_name="Accession Image Description")
    keyword = models.ManyToManyField(
        Keyword, related_name="keywords",)
    downloadable = models.BooleanField(default=False)

    def __str__(self):
        return self.obj_name

    class Meta:
        verbose_name = "Catalog Item"
        verbose_name_plural = "Catalog Items"
