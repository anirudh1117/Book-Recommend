from django.db import models

class Recommend(models.Model):
    book = models.ForeignKey( "Books.Books", on_delete=models.CASCADE)
    Celebrity = models.ForeignKey( "Celebrity.Celebrity", on_delete=models.CASCADE)
    celebrityComment = models.TextField()
    recommendedDate = models.DateTimeField()
    source = models.URLField()

    def __str__(self):
        return f'{self.book}' 
