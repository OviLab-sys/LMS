from django.db import models
from books.models import Books
from students.models import Student


class Borrowing(models.Model):
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        related_name='borrowed_books'
    )
    book = models.ForeignKey(
        Books, 
        on_delete=models.CASCADE, 
        related_name='borrowed_by_students'
    )
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'student', 'return_date'],
                name='unique_active_borrowing_borrow'
            )
        ]
    
    def __str__(self):
        return f"{self.student.name} - {self.book.title} - {self.due_date}"