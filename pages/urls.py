from django.urls import path
from django.views.generic import TemplateView

from .views import (
    HomeView,
    contact_us_form,
    volunteer_form,
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
    wgnas_page,
    wgnas_photo_list,
    wgnas_photo_detail,
    wgnas_photo_comment,
    napc_page,
    napc_photo_list,
    napc_photo_detail,
    napc_photo_comment,
    donate_page,
    confirm_donation,
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
        "contact-us-submit",
        contact_us_form,
        name="contact_us_form",
    ),
    path(
        "volunteer",
        TemplateView.as_view(template_name="pages/volunteer.html"),
        name="volunteer",
    ),
    path(
        "volunteer-form",
        volunteer_form,
        name="volunteer_form",
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
    path(
        "lavelle-aircraft-corp",
        TemplateView.as_view(template_name="pages/projects/lavelle-aircraft-corp.html"),
        name="lavelle_aircraft_corp",
    ),
    path(
        "donate",
        donate_page,
        name="donate",
    ),
    path(
        "confirm-donation",
        confirm_donation,
        name="confirm_donation",
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
    ## NADC ##
    path("projects/naval-air-development-center", nadc_page, name="nadc"),
    path(
        "projects/naval-air-development-center/photo-archive",
        nadc_photo_list,
        name="nadc_photo_list",
    ),
    path(
        "projects/naval-air-development-center/photo-archive/<tag>/",
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
        TemplateView.as_view(
            template_name="pages/projects/nadc_15th_reunion.html"),
        name="nadc_15th_reunion",
    ),
    path(
        "projects/naval-air-development-center/20th-reunion",
        TemplateView.as_view(
            template_name="pages/projects/nadc_20th_reunion.html"),
        name="nadc_20th_reunion",
    ),
    path(
        "projects/naval-air-development-center/25th-reunion",
        TemplateView.as_view(
            template_name="pages/projects/nadc_25th_reunion.html"),
        name="nadc_25th_reunion",
    ),
    path(
        "projects/naval-air-development-center/alumni-reception",
        TemplateView.as_view(
            template_name="pages/projects/nadc_alumni_reception.html"),
        name="nadc_alumni_reception",
    ),
    ## WGNAS ##
    path("projects/willow-grove-naval-air-station", wgnas_page, name="wgnas"),
    path(
        "projects/willow-grove-naval-air-station/photo-archive",
        wgnas_photo_list,
        name="wgnas_photo_list",
    ),
    path(
        "projects/willow-grove-naval-air-station/photo-archive/<tag>/",
        wgnas_photo_list,
        name="wgnas_photo_list",
    ),
    path(
        "projects/willow-grove-naval-air-station/photo-archive/<int:pk>",
        wgnas_photo_detail,
        name="wgnas_photo_detail",
    ),
    path(
        "projects/willow-grove-naval-air-station/photo-archive/<int:pk>/comment",
        wgnas_photo_comment,
        name="wgnas_photo_comment",
    ),
    ## NAPC ##
    path("projects/naval-air-propulsion-center", napc_page, name="napc"),
    path(
        "projects/naval-air-propulsion-center/photo-archive",
        napc_photo_list,
        name="napc_photo_list",
    ),
    path(
        "projects/naval-air-propulsion-center/photo-archive/<tag>/",
        napc_photo_list,
        name="napc_photo_list",
    ),
    path(
        "projects/naval-air-propulsion-center/photo-archive/<int:pk>",
        napc_photo_detail,
        name="napc_photo_detail",
    ),
    path(
        "projects/naval-air-propulsion-center/photo-archive/<int:pk>/comment",
        napc_photo_comment,
        name="napc_photo_comment",
    ),
    path(
        "projects/naval-air-propulsion-center/reunion-2022",
        TemplateView.as_view(
            template_name="pages/projects/napc_reunion_sept_2022.html"),
        name="napc_reunion_sept_2022",
    ),
    path(
        "projects/naval-air-propulsion-center/reunion-2023",
        TemplateView.as_view(
            template_name="pages/projects/napc_reunion_sept_2023.html"),
        name="napc_reunion_sept_2023",
    ),
    path(
        "projects/naval-air-propulsion-center/reunion-2025",
        TemplateView.as_view(
            template_name="pages/projects/napc_reunion_sept_2025.html"),
        name="napc_reunion_sept_2025",
    ),
]
