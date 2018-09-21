# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	AloAlo,
)


class AloAloCreateView(CreateView):

    model = AloAlo


class AloAloDeleteView(DeleteView):

    model = AloAlo


class AloAloDetailView(DetailView):

    model = AloAlo


class AloAloUpdateView(UpdateView):

    model = AloAlo


class AloAloListView(ListView):

    model = AloAlo

