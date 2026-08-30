
from django.shortcuts import render,get_object_or_404
from .models import Products


def indexproduct(request):
    return render(request,"contact.html")

def productdetail(request,pk):

    product = get_object_or_404(Products, pk=pk)
    return render(request, "prodetail.html", {"product": product})


