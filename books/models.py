from django.db import models



class Book(models.Model):
    GENRE = (
        ('Детектив', 'Детектив'),
        ('Мистика', 'Мистика'),
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.FloatField(default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=10, choices=GENRE)
    author_email = models.EmailField(default=0)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book/')
    video_url = models.URLField(null=True)



    def __str__(self):
        return self.title


class Comments(models.Model):
    GRADE = (
        ('👍', '👍'),
        ('👍👍', '👍👍'),
        ('👍👍👍', '👍👍👍'),
        ('👍👍👍👍', '👍👍👍👍'),
        ('👍👍👍👍👍', '👍👍👍👍👍'),
    )
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE,
                                    related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    grade = models.CharField(max_length=10, choices=GRADE, default='👍')