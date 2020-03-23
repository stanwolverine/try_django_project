"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from pages.views import home_view, about_view, contact_view, social_view
from products.views import product_detail_view, product_create_view

urlpatterns = [
    path('', home_view, name='home-view'),
    path('blog/', include('blog.urls')),
    path('about/', about_view, name='about-view'),
    path('contact/', contact_view, name='contact-view'),
    path('social/', social_view, name='social-view'),
    path('product/', product_detail_view, name='product-detail-view'),
    path('create/', product_create_view, name='product-create-view'),
    path('admin/', admin.site.urls),
]
