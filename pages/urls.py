from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, EventList, event_detail

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
]
