from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request,'portfolio_website/templates/home.html')

def home(request):
    return render(request, 'home.html')

from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        subject = f'Portfolio Contact Form Submission from {name}'
        message = f'Name: {name}\nEmail: {email}\nPhone: {number}\nMessage: {content}'
        recipient = ['roshanidaulkar1@gmail.com']

        try:
            send_mail(subject, message, email, recipient)
            return JsonResponse({'status':'success'})
        except Exception as e:
            return JsonResponse({'status':'fail', 'error': str(e)}, status=500)
    return JsonResponse({'status':'invalid'}, status=400)
