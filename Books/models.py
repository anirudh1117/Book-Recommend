from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class SubCategory(models.Model):
    name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return f'{self.name}' 

class Categories(models.Model):
    name = models.CharField(max_length=100,blank=False)
    SubCategories = models.ManyToManyField('SubCategory')

    def __str__(self):
        return f'{self.name}' 

class Books(models.Model):
    name = models.CharField(max_length=100,blank=False)
    title = models.CharField(max_length=256,blank=False)
    authorName = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    categories = models.ManyToManyField('Categories')
    ISBN = models.CharField(max_length=100,blank=True)
    ratings = models.ManyToManyField('Rating')
    dateOfPublish = models.DateTimeField()

    def __str__(self):
        return f'{self.name}' 



class BookImages(models.Model):
    book = models.ForeignKey( "Books", on_delete=models.CASCADE)
    image = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)

class Rating(models.Model):
    name = models.CharField(max_length=100,blank=False)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    book = models.ForeignKey( "Books", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}' 


COMPANY_CHOICES = (
    ("AMAZON", "AMAZON"),
    ("FLIPKART", "FLIPKART"),
)

class AffillateLink(models.Model):
    companyName = models.CharField(max_length=100,blank=False,choices = COMPANY_CHOICES)
    link = models.URLField()
    book = models.ForeignKey( "Books", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.companyName}' 
    