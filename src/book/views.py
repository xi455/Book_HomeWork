from rest_framework import viewsets

from book.models import Book, Borrower, BorrowingRecord
from book.serializers import BookSerializer, BorrowerSerializer, BorrowingRecordSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BorrowerViewSet(viewsets.ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer


class BorrowingRecordViewSet(viewsets.ModelViewSet):
    queryset = BorrowingRecord.objects.all()
    serializer_class = BorrowingRecordSerializer