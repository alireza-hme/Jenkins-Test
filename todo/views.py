from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoCreateView(APIView):
    def post(self, request):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDeleteView(APIView):
    def delete(self, request, pk):
        todo = get_object_or_404(ToDo, pk=pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
