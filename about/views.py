from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
# class AboutList(generic.ListView):
#     queryset = About.objects.all().order_by('-updated_on')
#     template_name = "about/about_list.html"


def about_me(request):
    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                (
                    "Collaboration request received! "
                    "I endeavor to respond within 2 working days."
                )
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error with your submission'
            )

    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form
        },
    )
