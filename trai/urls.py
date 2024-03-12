from django.urls import path
from . import views

urlpatterns = [
    path('train-book/', views.train_book, name='train_book'),
]
