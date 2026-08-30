from django.urls import path
from .views import indexproduct, productdetail
from django.urls import path
from .views import *
urlpatterns = [
    path('', indexproduct, name='indexproduct'),
    path('detail/<int:pk>/', productdetail, name='prodetail'),
]

