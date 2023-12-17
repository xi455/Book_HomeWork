from django.contrib import admin
from book.models import Book, Borrower, BorrowingRecord
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'isbn',
        'published_date',
        'genre',
        'quantity_in_stock',
        'price',
        'description',
    )
    list_filter = ('published_date',)


@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address')
    search_fields = ('name',)


@admin.register(BorrowingRecord)
class BorrowingRecordAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'book',
        'borrower',
        'borrow_date',
        'return_date',
        'actual_return_date',
        'fine_amount',
    )
    list_filter = (
        'book',
        'borrower',
        'borrow_date',
        'return_date',
        'actual_return_date',
    )
