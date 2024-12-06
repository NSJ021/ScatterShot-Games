"""
Views for the ssg_contact app.
"""
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserMessage
from django.conf import os


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

        # Send email to admin
        # Retrieve all superuser emails
        admin_emails = list(User.objects.filter(
            is_superuser=True).values_list('email', flat=True))

        # Email details
        admin_message = f"""
                Hello Admin,

                You have received a new message,
                from a user of ScatterShot Games.

                Details of the message:
                - Name: {name}
                - Email: {email}
                - Subject: {subject}
                - Phone Number: {phone_number}

                Message:
                {message}

                Please check the User Messages Section,
                Located within the admin panel for more details.

                Best regards,
                Team ScatterShot
                """

        # Send email
        send_mail(
            subject,
            admin_message,
            os.environ.get('EMAIL_HOST_USER'),  # Sender Address
            admin_emails,  # Recipient List
            fail_silently=False,
        )

        # Email details for user
        user_message = f"""
                Hello {name},

                Thank you for contacting ScatterShot Games.

                We have received your message,
                We will get back to you as soon as possible.

                Details of your message:
                - Subject: {subject}
                - Phone Number: {phone_number}

                Message:
                {message}

                Best regards,
                Team ScatterShot
                """

        # Send email to user
        send_mail(
            'Thank you for contacting ScatterShot Games',
            user_message,
            os.environ.get('EMAIL_HOST_USER'),  # Sender Address
            [email],  # Recipient List
            fail_silently=False,
        )

        # Save the message
        new_contact.save()
        messages.success(request, 'Your message has been sent successfully')

        # Render the contact page template
        return redirect('contact')
    else:
        # Render the contact page template
        return render(request, 'ssg_contact/contact.html')
