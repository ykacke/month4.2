from django import forms
from parser import models, parser_manga, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('remanga.org', 'remanga.org'),
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


    class Meta:
        fields = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'remanga.org':
            manga_book = parser_manga.parsing_manga()
            for i in manga_book:
                models.MangaModel.objects.create(**i)

        elif self.data['media_type'] == 'rezka.ag':
            rezka_films = parser_rezka.parsing_rezka()
            print(rezka_films)
            for i in rezka_films:
                models.RezkaFilmsModel.objects.create(**i)