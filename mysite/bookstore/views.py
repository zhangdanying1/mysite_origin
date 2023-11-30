from django.shortcuts import render
from oscar.core.loading import get_model

ProductImage = get_model('catalogue', 'ProductImage')


def product_display(request):
    image_list = ProductImage.objects.order_by('product_id', '-date_created').distinct('product_id')
    return render(request, 'bookstore/index.html', {'image_list': image_list})
