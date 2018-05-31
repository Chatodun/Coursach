from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Твердый переплёт'),
        (PAPERBACK, 'Мягкий переплёт'),
        (EBOOK, 'Электронная книга'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(blank=True, null=True)
    author = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    pages = models.IntegerField(blank=True, null=True)
    book_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES, blank=True, null=True)
