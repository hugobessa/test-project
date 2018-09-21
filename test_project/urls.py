# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'test_project'
urlpatterns = [
    url(
        regex="^AloAlo/~create/$",
        view=views.AloAloCreateView.as_view(),
        name='AloAlo_create',
    ),
    url(
        regex="^AloAlo/(?P<pk>\d+)/~delete/$",
        view=views.AloAloDeleteView.as_view(),
        name='AloAlo_delete',
    ),
    url(
        regex="^AloAlo/(?P<pk>\d+)/$",
        view=views.AloAloDetailView.as_view(),
        name='AloAlo_detail',
    ),
    url(
        regex="^AloAlo/(?P<pk>\d+)/~update/$",
        view=views.AloAloUpdateView.as_view(),
        name='AloAlo_update',
    ),
    url(
        regex="^AloAlo/$",
        view=views.AloAloListView.as_view(),
        name='AloAlo_list',
    ),
	]
