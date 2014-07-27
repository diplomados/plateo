from django.test import TestCase
from django.contrib.auth.models import User
from .models import Curso
# Create your tests here.


class ClasesTest(TestCase):

    """docstring for ClasesTest"""
    
    def setUp(self):
        self.user = User.objects.create(
            username="asullom",
            password="12345",
            email="asullom@gmail.com"
        )

    def test_add_curso(self):

        curso = Curso(
            nombre="Django Profesional",
            slug="django-profesional"
            # usuario=self.user
        )
        curso.save()
        r = Curso.objects.first()
        self.assertEqual(r.nombre, "Django Profesional")
