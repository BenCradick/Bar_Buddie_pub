from charges.models import Charge
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
 
from charges.serializers import TodoSerializer
 
 
class ChargesList(generics.ListCreateAPIView):
    queryset = Charges.objects.all()
    serializer_class = ChargesSerializer
 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
 
 
class ChargesDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChargesSerializer
 
    def get_queryset(self):
        return Charges.objects.all().filter(user=self.request.user)