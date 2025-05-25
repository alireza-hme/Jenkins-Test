from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoViewSet(
    mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
