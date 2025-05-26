from django.urls import path
from .views import ToDoCreateView, ToDoDeleteView

urlpatterns = [
    path("api/todos/", ToDoCreateView.as_view(), name="todo-create"),
    path("api/todos/<int:pk>/", ToDoDeleteView.as_view(), name="todo-delete"),
]
