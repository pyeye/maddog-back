from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Menu

class MenuTests(APITestCase):
    def setUp(self):
        Menu.objects.create(name="Стейк", description="test description1", detail={"category": "test"})
        Menu.objects.create(name="Уха", description="test description2", detail={"category": "test2"})

    def test_get_all_menu(self):
        response = self.client.get('/api/v1/menu/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.filter(is_active=True).count(), len(response.data))

    def test_get_first_menu(self):
        response = self.client.get('/api/v1/menu/3/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('Стейк', response.data['name'])

    def test_not_found_menu(self):
        response = self.client.get('/api/v1/menu/113/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
