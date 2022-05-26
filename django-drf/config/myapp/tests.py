from django.test import TestCase
from django.urls import reverse
from rest_framework import status



class TestArticleView(TestCase):
	def setUp(self):
		self.client.login(username = "admin", password="1234")

	def test_authintication_required(self):
		self.client.logout()
		url = reverse("question_list")
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
