from django.test import TestCase
from app import models

class test_crud(TestCase):
    def test_create(self):
        test = models.CRUD.create("Joe", 23, "2000-11-11")
        self.assertEqual(test.name, "Joe")
        self.assertEqual(test.age, 23)
        self.assertEqual(test.dob, "2000-11-11")
    def test_read(self):
        self.assertEqual(models.CRUD.objects, models.CRUD.read())
    def test_readByName(self):
        test = models.CRUD.create("Joe", 23, "2000-11-11")
        self.assertEqual(models.CRUD.readByName('Joe').first(), models.CRUD.objects.get(name="Joe"))
    def test_delete(self):
        test = models.CRUD.create("Joe", 23, "2000-11-11")
        models.CRUD.deleteItem('Joe')
        self.assertFalse(models.CRUD.objects.exists())
    def test_update(self):
        test = models.CRUD.create("Joe", 23, "2000-11-11")
        self.assertEqual(models.CRUD.objects.first().name, "Joe")
        models.CRUD.update('Joe','Jeff',24,'1999-11-11')
        self.assertEqual(models.CRUD.objects.first().name, "Jeff")