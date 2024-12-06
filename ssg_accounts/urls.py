"""
URL configuration for the SSG Accounts application.

This module defines the URL patterns for the games application,
mapping URLs to views.
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'ssg_accounts'

urlpatterns = [
    # User authentication views
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Password reset views
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='ssg_accounts/password_reset_form.html',
            email_template_name='ssg_accounts/password_reset_email.html',
            success_url='/accounts/password_reset/done/',
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='ssg_accounts/password_reset_done.html'
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='ssg_accounts/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
]
