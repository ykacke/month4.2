from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me),
    path('about_animal/', views.about_animal),
    path('animal_image/', views.animal_image),
    path('time/', views.time),
]