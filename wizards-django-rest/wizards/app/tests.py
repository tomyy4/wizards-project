from django.test import TestCase
from app.models import House, Wizard, Founder
from django.db.utils import IntegrityError

class TestWizard(TestCase):
    def test_cannot_create_wizards_with_the_same_name(self):
        f = Founder.objects.create(name='Goddric')
        h = House.objects.create(name='Griffindor', founder=f)
        Wizard.objects.create(name='Harry', house=h)
        with self.assertRaises(IntegrityError):
            Wizard.objects.create(name='Harry', house=h)


class HouseTest(TestCase):
    def test_cannot_create_house_with_the_same_name(self):
        f = Founder.objects.create(name='Goddric')
        House.objects.create(name='Griffindor', founder=f)
        with self.assertRaises(IntegrityError):
            House.objects.create(name='Griffindor', founder=f)