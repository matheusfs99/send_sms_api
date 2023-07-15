from rest_framework import serializers
from .models import Contacts, GroupContacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = "__all__"


class GroupContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupContacts
        fields = "__all__"
