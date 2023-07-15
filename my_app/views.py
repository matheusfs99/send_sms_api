from .serializers import ContactSerializer, GroupContactsSerializer
from rest_framework import viewsets, permissions
from .models import Contacts, GroupContacts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from twilio.rest import Client
from django.conf import settings


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contacts.objects.all()
    permission_classes = [permissions.AllowAny]


class GroupContactsViewSet(viewsets.ModelViewSet):
    serializer_class = GroupContactsSerializer
    queryset = GroupContacts.objects.all()
    permission_classes = [permissions.AllowAny]


@api_view(["POST"])
def send_sms(request):
    if "group" not in request.data:
        return Response({"msg": "group is required"}, status=400)
    group = GroupContacts.objects.filter(id=request.data["group"]).first()
    contact_names = []
    if group:
        contacts = group.contacts.all()
        for contact in contacts:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            client.messages.create(
                from_=settings.TWILIO_PHONE_NUMBER,
                to=contact.phone,
                body=f"Olá {contact.name}, você acaba de ganhar 1 milhão de reais! Parabéns! Pode pagar o agiota em paz."
            )
            contact_names.append(contact.name)
    return Response({"msg": f"sms enviado com sucesso para {contact_names}!"})
