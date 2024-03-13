from django.shortcuts import render

def train_book(request):
    return render(request, 'train-book.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def successful(request):
    return render(request, 'successful.html')

def train_bookingsystem(request):
    return render(request, 'train-bookingsystem.html')

def train_confirm_details(request):
    return render(request, 'train-confirm-details.html')

def train_email(request):
    return render(request, 'train-email.html')

def train_grid(request):
    return render(request, 'train-grid.html')

def train_invoice(request):
    return render(request, 'train-invocie.html')

def train_list(request):
    return render(request, 'train-list.html')

def train_oneway(request):
    return render(request, 'train-oneway.html')

def train_payment(request):
    return render(request, 'train-payment.html')

def personal_information(request):
    return render(request, 'personal-information.html')




