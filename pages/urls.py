from django.urls import path
from django.views.generic import TemplateView

from .views import (
    HomeView,
    hiob_events,
    movie_night_events,
    avt_events,
    other_events,
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
    path(
        "merchandise",
        TemplateView.as_view(template_name="pages/merchandise.html"),
        name="merchandise",
    ),
    path(
        "links",
        TemplateView.as_view(template_name="pages/links.html"),
        name="links",
    ),
    ### EVENTS ###
    path("events/history-in-our-backyard", hiob_events, name="hiob_events"),
    path("events/movie-nights", movie_night_events, name="movie_events"),
    path("events/annual-veterans-tribute", avt_events, name="avt_events"),
    path("events/other-activities", other_events, name="other_events"),
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
    path(
        "projects/naval-air-development-center/15th-reunion",
        TemplateView.as_view(template_name="pages/projects/nadc_15th_reunion.html"),
        name="nadc_15th_reunion",
    ),
]
