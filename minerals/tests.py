from django.test import TestCase
from django.utils import timezone
# Create your tests here.

from .models import  Mineral

class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Ben's Test Mineral"
        )
        self.assertIn(mineral, Mineral.objects.all())

