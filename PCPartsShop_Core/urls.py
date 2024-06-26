"""
URL configuration for PCPartsShop_Core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from routers import router

from apps.login.views import LoginView
from apps.users.views import UserListCreate, UserRetrieveUpdateDestroy
from apps.products.views import ProductSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'core_api'), namespace='core_api')),
    path('api/users/', UserListCreate.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-details'),
    path('api/products/search/<str:q>/', ProductSearch, name='product-search'),
    path('api/login/', LoginView.as_view(), name='login'),
]
