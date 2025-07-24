from django.shortcuts import render
from .models import About


# Create your views here.
# class AboutList(generic.ListView):
#     queryset = About.objects.all().order_by('-updated_on')
#     template_name = "about/about_list.html"


def about_detail(request):
    """
    Display the about page.

    **Context**

    ``about``
        An instance of :model:`about.About`.

    **Template:**

    :template:`about/about_detail.html`
    """

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )