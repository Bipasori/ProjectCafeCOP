from django.db import models

class Book(models.Model):
    BOOK_TYPES = (
        ("HD", '하드카바'),
        ("PB", '종이책'),
        ("EB", '전자책'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.CharField(choices=BOOK_TYPES,max_length=20)

    class Meta:
        db_table = "myapp_book"

