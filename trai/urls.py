from django.urls import path
from .views import train_book

urlpatterns = [
    path('', train_book, name='train_book'),  # Remove the extra space in the path pattern
]
