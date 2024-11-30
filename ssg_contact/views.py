"""
Views for the ssg_contact app.
"""
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserMessage


# Create your views here.

def user_contact(request):
    """
    Renders the contact page.
    """
    if request.method == 'POST':
        # Get the form data
        user = request.user if request.user.is_authenticated else None
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone_number = request.POST['phone']
        message = request.POST['message']

        # Save new User message
        new_contact = UserMessage(user_id=user.id if user else None,
                                  name=name, email=email, subject=subject,
                                  phone_number=phone_number,
                                  message=message)

        # Save the message
        new_contact.save()
        messages.success(request, 'Your message has been sent successfully')

        # Render the contact page template
        return redirect('contact')
    else:
        # Render the contact page template
        return render(request, 'ssg_contact/contact.html')
