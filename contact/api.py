from rest_framework.viewsets import ModelViewSet
from .serializers import ContactSerializers
from .models import Contact

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers
