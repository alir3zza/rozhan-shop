from django.shortcuts import render

from home.models import Product
from django.core.paginator import Paginator

def index(request):
    data = Product.objects.all()

    paginator=Paginator(data,4)

    page_number=request.GET.get('page')

    page_obj=paginator.get_page(page_number)

    return render(request, "index.html",{"data":data})

