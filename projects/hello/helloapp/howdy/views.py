from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    #def get(self, request, **kwargs):
        #return render(request, 'index.html', context=None)
    template_name = "index.html"

# Add this view
class AboutPageView(TemplateView):
    template_name = "about.html"
