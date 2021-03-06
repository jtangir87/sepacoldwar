from django.contrib import admin
from .models import (
    Event,
    EventPhoto,
    EventDescriptions,
    OralHistoriesPage,
    DynamicFlightSimulatorPage,
    NADCPhotoPage,
    NADCPhoto,
    NADCPhotoComment,
)
from django.conf import settings

# Register your models here.
class NADCPhotoCommentAdmin(admin.ModelAdmin):
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
    admin.site.register(NADCPhoto)
    admin.site.register(NADCPhotoComment, NADCPhotoCommentAdmin)

else:
    admin.site.register(DynamicFlightSimulatorPage)
    admin.site.register(OralHistoriesPage)
    admin.site.register(Event)
    # admin.site.register(EventPhoto)
    admin.site.register(EventDescriptions)
    admin.site.register(NADCPhotoPage)
    admin.site.register(NADCPhoto)
    admin.site.register(NADCPhotoComment, NADCPhotoCommentAdmin)