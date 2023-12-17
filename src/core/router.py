from rest_framework import routers

from book import views as book_views

router = routers.SimpleRouter()
router.register("books", book_views.BookViewSet)
router.register("borrowers", book_views.BorrowerViewSet)
router.register("borrowingrecords", book_views.BorrowingRecordViewSet)