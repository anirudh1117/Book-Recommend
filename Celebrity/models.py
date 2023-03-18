from django.db import models

class Profession(models.Model):
    name = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return f'{self.name}' 

class Celebrity(models.Model):
    name = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    professions = models.ManyToManyField('Profession')
    image = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True)


    def __str__(self):
        return f'{self.name}' 



PLATFORM_CHOICES = (
    ("INSTAGRAM", "INSTAGRAM"),
    ("TWITTER", "TWITTER"),
    ("FACEBOOK", "FACEBOOK"),
)

class SocialPlatform(models.Model):
    Celebrity = models.ForeignKey( "Celebrity", on_delete=models.CASCADE)
    name = models.CharField(max_length=100,choices = PLATFORM_CHOICES)
    link = models.URLField()

    def __str__(self):
        return f'{self.name}' 
    