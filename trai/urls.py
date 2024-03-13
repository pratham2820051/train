from django.urls import path
from .views import train_book, about, signin, signup, successful,train_bookingsystem, train_confirm_details, train_email, train_grid, train_invoice, train_list, train_oneway, train_payment, personal_information
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', train_book, name='train_book'),
    path('about.html', about, name='about.html'),
    path('signin.html', signin, name='signin.html'),
    path('signup.html', signup, name='signup.html'),
    path('sucessful.html', successful, name='successful.html'),
    path('train-bookingsystem.html', train_bookingsystem, name='train_bookingsystem'),
    path('train-confirm-details.html', train_confirm_details, name='train_confirm_details'),
    path('train-email.html', train_email, name='train_email.html'),
    path('train_grid', train_grid, name='train_grid'),
    path('train_invocie', train_invoice, name='train_invocie'),
    path('train_list', train_list, name='train_list'),
    path('train-oneway', train_oneway, name='train_oneway'),
    path('train_payment', train_payment, name='train_payment'),
    path('personal-information.html', personal_information, name='personal_information.html'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
  
