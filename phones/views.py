import operator
from pprint import pprint

from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()

    sort = request.GET.get('sort')
    if sort == 'price_min':
        sorted_phones = sorted(phones, key=operator.attrgetter('price'))
    elif sort == 'price_max':
        sorted_phones = sorted(phones, key=operator.attrgetter('price'), reverse=True)
    elif sort == 'name_first_a':
        sorted_phones = sorted(phones, key=operator.attrgetter('name'))
    elif sort == 'name_first_z':
        sorted_phones = sorted(phones, key=operator.attrgetter('name'), reverse=True)

    context = {'phones': sorted_phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    phone_query = Phone.objects.filter(slug=slug)

    context = {
        'info_phone': phone_query[0]
    }
    return render(request, template, context)
