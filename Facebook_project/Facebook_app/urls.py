"""
URL configuration for Facebook_project project.

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
from django.urls import path,include
from .views import facebook_profile_view , post_to_facebook,fetch_page_insights
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('facebook/profile/', facebook_profile_view, name='facebook_profile'),
    path('facebook/pagepost/',post_to_facebook,name='post_to_facebook'),
    path('facebook/pageinsights/',fetch_page_insights,name='fetch_page_insights')
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
