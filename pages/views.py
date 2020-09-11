from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from datetime import date

from .models import Event

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        context["events"] = Event.objects.filter(date__gte=today)
        return context


class EventList(TemplateView):
    template_name = "pages/events.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        context["upcoming_events"] = Event.objects.filter(date__gte=today)
        context["past_events"] = Event.objects.filter(date__lt=today)
        return context


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, "pages/event_detail.html", {"event": event})