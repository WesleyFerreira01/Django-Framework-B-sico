from rest_framework import viewsets
from books.api.serializers import BooksSerializer
from books.models import books


class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()
