from django.test import TestCase
from django.urls import reverse


# Create your tests here.

from .models import  Mineral

class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Mineral.objects.create(
            name="Ben's Test Mineral"
        )
        self.assertIn(mineral, Mineral.objects.all())


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Bens Rock",
            category="Mineral Testing",
            group="Organic",
            diaphaneity="Wonderful"
        )
        self.mineral2 = Mineral.objects.create(
            name="Bens Really Cool Rock",
            category="Mineral Mining",
            group="Fake Rocks",
            diaphaneity="What does that even mean?"
        )

    #testing views!
    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)
        self.assertContains(resp, self.mineral2.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])