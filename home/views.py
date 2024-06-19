from django.shortcuts import render

from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html' # specificam calea fisierului .html pe care o dorim randata/afisata.
