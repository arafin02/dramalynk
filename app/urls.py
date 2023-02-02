from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("drama/<slug:slug>", view=views.details, name="details"),
    path("drama/ep/<slug:ep_slug>", view=views.episode_detail, name="episode"),
    path("genre/<str:name>/", view=views.genrePage, name="genre"),
    path("search",
         views.searchPage, name="search"),


]
