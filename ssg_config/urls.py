"""
URL configuration for ssg_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', include('ssg_games.urls')),
    path('blog/', include('ssg_blog.urls')),
    path('contact/', include('ssg_contact.urls')),
    path('accounts/', include('ssg_accounts.urls', namespace='ssg_accounts')),
    path('socialaccounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('ssg_pages.urls')),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='ssg_accounts/password_reset_complete.html'
        ),
        name='password_reset_complete',
    ),
]
