from django.urls import path
from . import views


urlpatterns = [
    path('all_tags_films/', views.all_category_book, name='all'),
    path('comedy_tags_films/', views.children_books, name='comedy'),
    path('fantastic_tags_films/', views.teen_books, name='detective'),
]