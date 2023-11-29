from django.db import models
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct):
    book_url = models.URLField(default=False)

    class Meta(AbstractProduct.Meta):
        ordering = ['-id']

    def __str__(self):
        return self.title


from oscar.apps.catalogue.models import *
