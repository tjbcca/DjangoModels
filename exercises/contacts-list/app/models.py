from django.db import models

class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.TextField()
    is_favorite = models.BooleanField()
def create_contact(name,email,phone,is_favorite):
    a = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    a.save()
    return a
def all_contacts():
    return Contact.objects.all()
def find_contact_by_name(name):
    try:
        return Contact.objects.get(name=name)
    except:
        return None
def favorite_contacts():
    return Contact.objects.filter(is_favorite=True)
def update_contact_email(name, new_email):
    Contact.objects.filter(name=name).update(email=new_email)
def delete_contact(name):
    Contact.objects.get(name=name).delete()