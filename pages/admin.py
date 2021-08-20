from django.contrib import admin
from .models import (
    Event,
    EventPhoto,
    EventDescriptions,
    OralHistoriesPage,
    DynamicFlightSimulatorPage,
    NADCPhotoPage,
    WGNASPhotoPage,
    NAPCPhotoPage,
    NADCPhoto,
    NADCPhotoComment,
    NAPCPhoto,
    NAPCPhotoComment,
    WGNASPhoto,
    WGNASPhotoComment,
    PhotoTag
)
from django.conf import settings

# Register your models here.


class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "approved")
    list_filter = ["approved"]


class RemoveAddPersmissionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


if settings.DEBUG == False:
    admin.site.register(OralHistoriesPage, RemoveAddPersmissionAdmin)
    admin.site.register(DynamicFlightSimulatorPage, RemoveAddPersmissionAdmin)
    admin.site.register(Event)
    # admin.site.register(EventPhoto)
    admin.site.register(EventDescriptions, RemoveAddPersmissionAdmin)
    admin.site.register(NADCPhotoPage, RemoveAddPersmissionAdmin)
    admin.site.register(WGNASPhotoPage, RemoveAddPersmissionAdmin)
    admin.site.register(NADCPhoto)
    admin.site.register(NAPCPhoto)
    admin.site.register(WGNASPhoto)
    admin.site.register(PhotoTag)
    admin.site.register(NADCPhotoComment, PhotoCommentAdmin)
    admin.site.register(NAPCPhotoComment, PhotoCommentAdmin)
    admin.site.register(WGNASPhotoComment, PhotoCommentAdmin)

else:
    admin.site.register(DynamicFlightSimulatorPage)
    admin.site.register(OralHistoriesPage)
    admin.site.register(Event)
    # admin.site.register(EventPhoto)
    admin.site.register(EventDescriptions)
    admin.site.register(NADCPhoto)
    admin.site.register(NADCPhotoPage)
    admin.site.register(NAPCPhoto)
    admin.site.register(NAPCPhotoPage)
    admin.site.register(WGNASPhoto)
    admin.site.register(WGNASPhotoPage)
    admin.site.register(PhotoTag)
    admin.site.register(NADCPhotoComment, PhotoCommentAdmin)
    admin.site.register(NAPCPhotoComment, PhotoCommentAdmin)
    admin.site.register(WGNASPhotoComment, PhotoCommentAdmin)
