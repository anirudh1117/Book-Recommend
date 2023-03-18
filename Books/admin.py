from django.contrib import admin
from .models import BookImages, Books, AffillateLink, SubCategory, Categories, Rating


admin.site.register(SubCategory)
admin.site.register(Categories)
admin.site.register(Books)
admin.site.register(BookImages)
admin.site.register(AffillateLink)
admin.site.register(Rating)
