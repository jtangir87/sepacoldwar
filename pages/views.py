from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from datetime import date

from .models import (
    Event,
    OralHistoriesPage,
    DynamicFlightSimulatorPage,
    NADCPhotoPage,
    NADCPhoto,
)

from .forms import PhotoCommentForm

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


def oral_histories_page(request):
    page = OralHistoriesPage.objects.all().first()
    return render(request, "pages/projects/oral_histories.html", {"page": page})


def dfs_page(request):
    page = DynamicFlightSimulatorPage.objects.all().first()
    return render(request, "pages/projects/dfs.html", {"page": page})


def nadc_page(request):
    context = {
        "text": NADCPhotoPage.objects.values_list("description", flat=True).first(),
        "photos": NADCPhoto.objects.all()[:4],
    }
    return render(request, "pages/projects/nadc.html", context)


def nadc_photo_list(request):
    photo_list = NADCPhoto.objects.all()
    page = request.GET.get("page", 1)

    paginator = Paginator(photo_list, 12)

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    context = {
        "photos": photos,
        "text": NADCPhotoPage.objects.values_list("description", flat=True).first(),
    }

    return render(request, "pages/projects/nadc_photo_list.html", context)


def nadc_photo_detail(request, pk):
    photo = get_object_or_404(NADCPhoto, pk=pk)
    form = PhotoCommentForm(initial={"photo": photo})

    context = {"photo": photo, "form": form}
    return render(request, "pages/projects/nadc_photo_detail.html", context)


def nadc_photo_comment(request, pk):
    photo = get_object_or_404(NADCPhoto, pk=pk)
    data = dict()
    if request.method == "POST":
        form = PhotoCommentForm(request.POST or None)
        if form.is_valid():
            form.save()

            data["html_success_message"] = render_to_string(
                "pages/projects/comment_success.html", request=request
            )
            data["form_is_valid"] = True

            return JsonResponse(data)