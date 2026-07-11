from http.client import responses
from first_app.models import Contact
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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
    else:
         form = ContactForm()
    return render(request, "website/contact.html", {"form":form})


def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponse("thanks")
    else:
        form = ContactForm()
    return render(request, "website/test.html", {"form":form})