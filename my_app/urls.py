from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, GroupContactsViewSet, send_sms


router = DefaultRouter()
router.register("contacts", ContactViewSet, basename="contacts")
router.register("groups", GroupContactsViewSet, basename="groups")

urlpatterns = [
    path("", include(router.urls)),
    path("send-sms/", send_sms, name="send-sms")
]
