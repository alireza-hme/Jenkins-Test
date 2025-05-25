from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import ToDo

# Create your tests here.


class ToDoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.todo = ToDo.objects.create(title="Test ToDo", is_done=False)

    def test_list_todos(self):
        response = self.client.get("/api/todos/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_todo(self):
        response = self.client.post(
            "/api/todos/", {"title": "New ToDo", "is_done": True}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ToDo.objects.count(), 2)

    def test_update_todo(self):
        response = self.client.patch(
            f"/api/todos/{self.todo.id}/", {"is_done": True}, format="json"
        )
        self.assertEqual(response.status_code, 200)
        self.todo.refresh_from_db()
        self.assertTrue(self.todo.is_done)

    def test_delete_todo(self):
        response = self.client.delete(f"/api/todos/{self.todo.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ToDo.objects.count(), 0)
