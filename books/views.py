from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from . import models
from .models import Book


def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id,
            }
        )


def books_list(request):
    if request.method == "GET":
        books = Book.objects.filter(genre='comedy')
        return render(
            request,
            template_name='book.html',
            context={
                'books': books,
            }
        )


def about_me(request):
    if request.method == "GET":
        return HttpResponse("меня зовут адэми, мне 20 лет")


def favorite_animal(request):
    if request.method == "GET":
        return HttpResponse(
            "Моё любимое животное кошка.Я люблю кошек за их грациозность и красоту,и ещё за их ловкость и быстроту.Кошки очень любят спать и играть.Кошки с мягкой шерстью,с красивыми и блестящими глазами и мощными лапами."

            "<''>")


def system_time(request):
    if request.method == "GET":
        now = datetime.datetime.now()
        return HttpResponse(f'текущее время {now}')