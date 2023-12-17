from rest_framework import serializers
from .models import Book, Borrower, BorrowingRecord

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'

class BorrowingRecordSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    borrower = BorrowerSerializer()

    class Meta:
        model = BorrowingRecord
        fields = '__all__'
