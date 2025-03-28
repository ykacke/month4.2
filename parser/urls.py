from django.urls import path
from . import views

urlpatterns = [
    path("manga_list/", views.MangaListView.as_view(), name="manga_list"),
    path("parser_form/", views.ParserForm.as_view(), name="parser_form"),
    path("rezka_list/", views.RezkaFilmListView.as_view(), name="rezka_list"),
    path("parser_form/", views.ParserForm.as_view(), name="parser_form"),
]