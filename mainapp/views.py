from django.shortcuts import render
from .utils import send_email

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        send_email(subject, email, message)
    return render(request, 'index.html')

