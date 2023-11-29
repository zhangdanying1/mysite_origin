from django.shortcuts import render
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')


def product_display(request, book_id):
    product_list = Product.objects.get(id=book_id)
    name = product_list.title
    return render(request, 'bookstore/index.html', {'name': name})
