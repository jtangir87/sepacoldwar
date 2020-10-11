from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import get_template
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.conf import settings
from datetime import date

from .models import (
    Event,
    EventDescriptions,
    OralHistoriesPage,
    DynamicFlightSimulatorPage,
    NADCPhotoPage,
    NADCPhoto,
)

from .forms import PhotoCommentForm, ContactForm, DonateForm


import stripe

stripe_pub_key = settings.STRIPE_PUBLISHABLE_KEY
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = date.today()
        context["events"] = Event.objects.filter(date__gte=today)
        return context


def donate_page(request):
    if request.method == "POST":
        form = DonateForm(request.POST or None)
        if form.is_valid():
            try:
                customer = stripe.Customer.create(
                    email=form.cleaned_data["email"],
                    name=form.cleaned_data["name"],
                    phone=form.cleaned_data["phone"],
                    source=request.POST["stripeToken"],
                )
            except stripe.error.CardError as e:
                # Since it's a decline, stripe.error.CardError will be caught
                body = e.json_body
                err = body["error"]
                stripe_error = err["message"]

                context = {
                    "stripe_pub_key": stripe_pub_key,
                    "form": DonateForm(request.POST),
                    "stripe_error": stripe_error,
                }
                return render(request, "pages/donate.html", context)
            amount = form.cleaned_data["amount"]
            context = {"customer_id": customer.id, "amount": amount}
            return render(request, "pages/donation_confirmation.html", context)
        else:
            errors = form.errors
            context = {
                "stripe_pub_key": stripe_pub_key,
                "form": DonateForm(request.POST),
                "errors": errors,
            }
    else:
        context = {"stripe_pub_key": stripe_pub_key, "form": DonateForm()}
    return render(request, "pages/donate.html", context)


def confirm_donation(request):
    if request.method == "POST":
        customer_id = request.POST.get("customer_id")
        stripe_amount = int(request.POST.get("amount")) * 100

        customer = stripe.Customer.retrieve(customer_id)
        charge = stripe.Charge.create(
            customer=customer,
            amount=stripe_amount,
            currency="usd",
            description="Donation",
        )

        ## EMAIL ELEANOR ##
        template = get_template("pages/donation_received.txt")
        context = {
            "name": customer.name,
            "phone": customer.phone,
            "email": customer.email,
            "amount": request.POST.get("amount"),
        }
        content = template.render(context)
        send_mail(
            "New Donation Received",
            content,
            "Donations <donotreply@elevatedwebsystems.com>",
            ["mail@coldwarhistory.org"],
            fail_silently=False,
        )

        ## EMAIL DONOR ##
        template = get_template("pages/donation_received_thank_you.txt")
        context = {
            "name": customer.name,
            "amount": request.POST.get("amount"),
        }
        content = template.render(context)
        send_mail(
            "Thank You For Your Donation",
            content,
            "Donations <mail@coldwarhistory.org>",
            [customer.email],
            fail_silently=False,
        )

        return render(request, "pages/thank_you.html")


def contact_us_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        template = get_template("pages/contact_us.txt")
        context = {
            "name": name,
            "phone": phone,
            "email": email,
            "message": message,
        }
        content = template.render(context)
        send_mail(
            "New Contact Us Submitted",
            content,
            "{}<{}>".format(name, email),
            ["mail@coldwarhistory.org"],
            fail_silently=False,
        )
        messages.success(request, "Success! Thank you for contacting us!")

    return redirect(reverse("contact_us"))


def volunteer_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")

        template = get_template("pages/contact_us.txt")
        context = {
            "name": name,
            "phone": phone,
            "email": email,
            "message": message,
        }
        content = template.render(context)
        send_mail(
            "New Volunteer Form",
            content,
            "{}<{}>".format(name, email),
            ["mail@coldwarhistory.org"],
            fail_silently=False,
        )
        messages.success(
            request,
            "Success! Thank you for your interest in becoming a volunteer! We will be in touch with you soon.",
        )

    return redirect(reverse("volunteer"))


def hiob_events(request):
    today = date.today()
    upcoming_events = Event.objects.filter(category="HIOB", date__gte=today)
    past_events = Event.objects.filter(category="HIOB", date__lt=today)
    description = EventDescriptions.objects.values_list("hiob", flat=True).first()
    return render(
        request,
        "pages/event_list_hiob.html",
        {
            "upcoming_events": upcoming_events,
            "past_events": past_events,
            "description": description,
        },
    )


def movie_night_events(request):
    today = date.today()
    upcoming_events = Event.objects.filter(category="MOVIE", date__gte=today)
    past_events = Event.objects.filter(category="MOVIE", date__lt=today)
    description = EventDescriptions.objects.values_list("movie", flat=True).first()
    return render(
        request,
        "pages/event_list_movie_night.html",
        {
            "upcoming_events": upcoming_events,
            "past_events": past_events,
            "description": description,
        },
    )


def avt_events(request):
    today = date.today()
    upcoming_events = Event.objects.filter(category="AVT", date__gte=today)
    past_events = Event.objects.filter(category="AVT", date__lt=today)
    description = EventDescriptions.objects.values_list("avt", flat=True).first()
    return render(
        request,
        "pages/event_list_avt.html",
        {
            "upcoming_events": upcoming_events,
            "past_events": past_events,
            "description": description,
        },
    )


def other_events(request):
    return render(
        request,
        "pages/event_list_other.html",
    )


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

            template = get_template("pages/comment_submitted.txt")
            context = {}
            content = template.render(context)
            send_mail(
                "New Photo Comment",
                content,
                "NADC Photo Comments <notreply@coldwarhistory.org>",
                ["mail@coldwarhistory.org"],
                fail_silently=False,
            )
            data["html_success_message"] = render_to_string(
                "pages/projects/comment_success.html", request=request
            )
            data["form_is_valid"] = True

            return JsonResponse(data)