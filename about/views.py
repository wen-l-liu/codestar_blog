from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
# class AboutList(generic.ListView):
#     queryset = About.objects.all().order_by('-updated_on')
#     template_name = "about/about_list.html"


def about_me(request):
    """
    Renders the most recent information about the website author 
    and allows user collaboration requests.
    Displays an individual instance of :model:`about.About`.
    **Context:**
    ``about``
        The most recent instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    **Template:**
    :template:`about/about.html`
    """
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
