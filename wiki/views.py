from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.template import loader
from .forms import PageForm


class PageList(ListView):
    """
    Display all instances of the Page model in a list. READ functionality
    for the whole Collection.
    """
    model = Page
    template_name = 'wiki/list.html'
    context_object_name = 'pages'


class PageDetailView(DetailView):
    """
    Display details of a single Wiki page featured on the site.

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the
          database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form
        fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse`
      function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the
      user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully
           updated.
    """
    model = Page
    template_name = 'wiki/page.html'
    context_object_name = 'page'

    def post(self, request, slug):
        pass
