"""
URL configuration for Book project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
# from Bookapp.views import BookDetails
from Bookapp.views import list_book,retrieve_book,create_book,update_book,delete_book

urlpatterns = [
    # Read operations
    path('Book/',list_book, name='list_book'),
    path('Book/<int:id>/',retrieve_book, name='retrieve_book'),

    # Create operation
    path('Book/create/',create_book, name='create_book'),

    # Update operation
    path('Book/update/<int:id>/',update_book, name='update_book'),

    # Delete operation
    path('Book/delete/<int:id>/',delete_book, name='delete_book'),
]
