from django.urls import path
from . import views

app_name = 'books' 

urlpatterns = [
    path('books', views.book_list,name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_detail'),
]