from django.db import models


class MangaModel(models.Model):
    title = models.CharField(max_length=500)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class RezkaFilmsModel(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', blank=True, null=True)


    def __str__(self):
        return self.title