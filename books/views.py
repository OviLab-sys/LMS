from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from django.views.decorators.csrf import csrf_exempt


def book_list(request):
    books = Books.objects.all()
    context = {'books':books}
    return render(request, 'books/book_list.html',context)

def book_detail(request, pk):
    book = get_object_or_404(Books,pk=pk)
    context = {'book': book}
    return render(request, 'books/book_detail.html', context)

@csrf_exempt
def book_create(request):
    if request.method =="POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')
        book = Books.objects.create(
            title = title,
            author = author,
            published_date = published_date,
            isbn = isbn
        )
        return redirect('book_detail', pk = book.id)
    return render(request,'books/book_form.html')

@csrf_exempt
def book_update(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.title = request.POST.get('title', book.title)
        book.author = request.POST.get('author', book.author)
        book.publish_date = request.POST.get('published_date', book.published_date)
        book.isbn =request.POST.get('isbn',book.ibn)
        book.save()
        return redirect('book_detail', pk=book.id)
    context = {
        'book':book,
    }
    return render(request, 'book/book_form.html', context)

@csrf_exempt
def book_delete(request, pk):
    book = get_object_or_404(Books, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    context = {
        'book':book
    }
    return render(request, 'books/book_confirm_delete.html', context)