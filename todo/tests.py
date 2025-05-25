from django.test import TestCase
from rest_framework.test import APIClient
from .models import ToDo

class ToDoAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_todo(self):
        response = self.client.post(
            "/api/todos/", {"title": "New ToDo", "is_done": True}, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ToDo.objects.count(), 1)

    def test_delete_todo(self):
        todo = ToDo.objects.create(title="To Delete", is_done=False)
        response = self.client.delete(f"/api/todos/{todo.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(ToDo.objects.count(), 0)
