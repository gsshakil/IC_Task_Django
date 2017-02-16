from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .api import ContactViewSet

router = DefaultRouter()
router.register(r'v1/contact', ContactViewSet)

urlpatterns = router.urls