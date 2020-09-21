from django.urls import path
from django.views.generic import TemplateView

from .views import (
    HomeView,
    EventList,
    event_detail,
    oral_histories_page,
    dfs_page,
    nadc_page,
    nadc_photo_list,
    nadc_photo_detail,
    nadc_photo_comment,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path(
        "about",
        TemplateView.as_view(template_name="pages/about_us.html"),
        name="about_us",
    ),
    path(
        "contact-us",
        TemplateView.as_view(template_name="pages/contact.html"),
        name="contact_us",
    ),
    path("events", EventList.as_view(), name="events"),
    path("events/<slug:slug>", event_detail, name="event_detail"),
    ## PROJECTS ##
    path(
        "projects/cold-war-oral-histories", oral_histories_page, name="oral_histories"
    ),
    path("projects/dynamic-flight-simulator", dfs_page, name="dfs"),
    path("projects/naval-air-development-center", nadc_page, name="nadc"),
    path(
        "projects/naval-air-development-center/photo-archive",
        nadc_photo_list,
        name="nadc_photo_list",
    ),
    path(
        "projects/naval-air-development-center/photo-archive/<int:pk>",
        nadc_photo_detail,
        name="nadc_photo_detail",
    ),
    path(
        "projects/naval-air-development-center/photo-archive/<int:pk>/comment",
        nadc_photo_comment,
        name="nadc_photo_comment",
    ),
]
