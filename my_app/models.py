from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class GroupContacts(models.Model):
    name = models.CharField(max_length=100)
    contacts = models.ManyToManyField("Contacts", related_name="contacts", null=True, blank=True)

    def __str__(self):
        return self.name
