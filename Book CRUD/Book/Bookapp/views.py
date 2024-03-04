from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.http import Http404
from .models import Book
from .serializer import BookSerializer

# Read (List and Retrieve) operations
@api_view(['GET'])
def list_book(request):
    if request.method == 'GET':
        obj = Book.objects.all()
        serializer_obj = BookSerializer(obj, many=True)
        return Response(serializer_obj.data)

@api_view(['GET'])
def retrieve_book(request, id):
    try:
        obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer_obj = BookSerializer(obj)
    return Response(serializer_obj.data)

# Create operation
@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        data = request.data
        serializer_obj = BookSerializer(data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

# Update operation
@api_view(['PUT'])
def update_book(request, id):
    try:
        obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = request.data
        serializer_obj = BookSerializer(obj, data=data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            return Response(serializer_obj.data)
        return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete operation
@api_view(['DELETE'])
def delete_book(request, id):
    try:
        obj = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        obj.delete()
        return Response({"response": "Book is successfully deleted."})
