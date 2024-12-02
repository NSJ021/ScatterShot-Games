"""
Views for the ssg_accounts app.
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import UsernameChangeForm, EmailChangeForm
from .forms import CustomPasswordChangeForm
from ssg_blog.models import Comment as BlogComment
from ssg_games.models import Comment as GameComment
from ssg_contact.models import UserMessage
from django.views.decorators.csrf import csrf_protect

# Create your views here.


# Signup view


def signup(request):
    """
    View for signing up the user.
    """
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        # Check if passwords match
        if password == confirm_password:
            # Check if username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('signup')
            else:
                # Check if email already exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('signup')
                else:
                    # Create user
                    user = User.objects.create_user(
                        username=username, password=password, email=email,
                        first_name=firstname, last_name=lastname)
                    # Login after register
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('ssg_accounts:dashboard')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'ssg_accounts/signup.html')

# Login view


@csrf_protect
def login(request):
    """
    View for logging in the user.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # Check if user exists
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('ssg_accounts:dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'ssg_accounts/login.html')

# Logout view


def logout(request):
    """
    View for logging out the user.
    """
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('home')


@login_required(login_url='login')
def dashboard(request):
    """
    View for the user dashboard.
    """
    if request.method == 'POST':
        username_form = UsernameChangeForm(request.POST, prefix='username')
        email_form = EmailChangeForm(request.POST, prefix='email')
        password_form = CustomPasswordChangeForm(
            user=request.user, data=request.POST, prefix='password')

        if username_form.is_valid() and 'username' in request.POST:
            new_username = username_form.cleaned_data['new_username']
            if User.objects.filter(username=new_username).exists():
                messages.error(request, 'Username already exists')
            else:
                try:
                    request.user.username = new_username
                    request.user.save()
                    messages.success(request, 'Username successfully changed!')
                except Exception as e:
                    messages.error(request, f'Failed to change username: {e}')
            return redirect('dashboard')

        if email_form.is_valid() and 'email' in request.POST:
            new_email = email_form.cleaned_data['new_email']
            if User.objects.filter(email=new_email).exists():
                messages.error(request, 'Email already exists')
            else:
                try:
                    request.user.email = new_email
                    request.user.save()
                    messages.success(request, 'Email successfully changed!')
                except Exception as e:
                    messages.error(request, f'Failed to change email: {e}')
            return redirect('dashboard')

        if password_form.is_valid() and 'password' in request.POST:
            user = password_form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Password successfully changed!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')

    else:
        username_form = UsernameChangeForm(prefix='username')
        email_form = EmailChangeForm(prefix='email')
        password_form = CustomPasswordChangeForm(
            user=request.user, prefix='password')
    # Get both types of comments
    blog_comments = BlogComment.objects.filter(
        author=request.user).select_related('post')
    game_comments = GameComment.objects.filter(
        author=request.user).select_related('game')
    user_messages = UserMessage.objects.filter(user_id=request.user)

    context = {
        'blog_comments': blog_comments,
        'game_comments': game_comments,
        'user_messages': user_messages,
        'is_superuser': request.user.is_superuser,
        'username_form': username_form,
        'email_form': email_form,
        'password_form': password_form,
    }
    return render(request, 'ssg_accounts/dashboard.html', context)


def password_reset(request):
    """
    View for resetting the user password.
    """
    return render(request, 'ssg_accounts/password_reset.html')


def password_reset_done(request):
    """
    View for password reset done.
    """
    return render(request, 'ssg_accounts/password_reset_done.html')


from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator


def test_password_reset_token(request, uidb64, token):
    try:
        # Decode the uidb64 to get the user ID
        uid = urlsafe_base64_decode(uidb64).decode()

        # Get the user from the decoded UID
        user = User.objects.get(pk=uid)

        # Validate the token
        is_valid = default_token_generator.check_token(user, token)

        return JsonResponse({
            'username': user.username,
            'is_valid': is_valid,
        })
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
