from django.shortcuts import render, get_object_or_404,redirect
from .models import Borrowing
from books.models import Books
from students.models import Student
from django.utils.timezone import now

def borrow_list(request):
    borrows = Borrowing.objects.all()
    context = {
        'borrows':borrows
    }
    return render(request, 'borrowing/borrow_list.html', context)

def borrow_book( request, student_id, book_id):
    student = get_object_or_404(Student, id=student_id)
    book= get_object_or_404(Books, id=book_id)
    
    #check if the book is availlable
    if Borrowing.objects.filter(book=book, is_returned=False).exists():
        return render( request, 'borrowing/borrow_error.html',{'message':'This book is already availlable.'})
    
    #create borrow record
    Borrowing.objects.create(student=student, book=book)
    return redirect('borrow_list')

#return a book
def return_book(request, borrow_id):
    borrow=get_object_or_404(Borrowing,id=borrow_id)
    borrow.is_returned=True
    borrow.return_date=now().date()
    borrow.save()
    return redirect('borrow_list')