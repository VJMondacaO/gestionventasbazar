from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

User = get_user_model()


class AuthAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.vendedor = User.objects.create_user(
            username='vendedor1',
            password='testpass123',
            rol='vendedor'
        )
        self.jefe_ventas = User.objects.create_user(
            username='jefe1',
            password='testpass123',
            rol='jefe_ventas'
        )
    
    def test_login_vendedor(self):
        response = self.client.post('/auth/login/', {
            'username': 'vendedor1',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.vendedor.is_authenticated)
    
    def test_login_jefe_ventas(self):
        response = self.client.post('/auth/login/', {
            'username': 'jefe1',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.jefe_ventas.is_authenticated)
    
    def test_rol_vendedor(self):
        self.assertTrue(self.vendedor.es_vendedor())
        self.assertFalse(self.vendedor.es_jefe_ventas())
    
    def test_rol_jefe_ventas(self):
        self.assertTrue(self.jefe_ventas.es_jefe_ventas())
        self.assertFalse(self.jefe_ventas.es_vendedor())
