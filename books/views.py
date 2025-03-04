from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def about_me(request):
    if request.method == "GET":
        return HttpResponse("<h1>I love you, baby <br> And if it's quite all right <br> I need you, baby <br> To warm these lonely nights <br> I love you, baby <br> Trust in me when I say</h1>")

def about_animal(request):
    if request.method == "GET":
        return HttpResponse("у меня нет животного но если введете /animal_image/ то увидите фотку рандомного животного")

def animal_image(request):
    if request.method == "GET":
        return HttpResponse("<img src= 'https://chikaspb.ru/upload/cssinliner_webp/iblock/072/dcjk3co223rcxp836oflbp9dqqjffpiw.webp'>")

def time(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")

