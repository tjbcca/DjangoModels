from django.db import models

class CRUD(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    dob = models.DateField()

    def create(name, age, dob):
        a = CRUD(name=name, age=age, dob=dob)
        a.save()
        return a

    def read():
        return CRUD.objects

    def readByName(name):
        return CRUD.objects.filter(name=name)

    def deleteItem(name):
        CRUD.objects.get(name=name).delete()

    def update(name, new, age, dob):
        CRUD.objects.filter(name=name).update(name=new, age=age, dob=dob)
