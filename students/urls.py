from django.urls import path
from . import views 

app_name = 'students'  # Define the app name for namespacing

urlpatterns = [
    path("books/", views.student_list, name='book_list'),
    path('books/<int:pk>/', views.student_detail, name='book_detail'),
    path('books/create/', views.student_create, name='book_create'),
    path('books/<int:pk>/update', views.student_update, name='book_update'),
    path('books/<int:pk>/delete/', views.student_delete, name='book_delete'),
]