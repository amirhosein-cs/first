from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

from first_app.forms import ContactForm


# Create your views here.


def index_view(request):
    return render(request, "website/index.html")


def about_view(request):
    return render(request, "website/about.html")


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Thank you! Your message has been sent."
            )

            return redirect("first_app:contact")

        messages.error(
            request,
            "Oops! Please check the form and try again."
        )

    else:
        form = ContactForm()
    return render(request, "website/contact.html", {"form": form})


def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("thanks")
    else:
        form = ContactForm()
    return render(request, "website/test.html", {"form": form})
