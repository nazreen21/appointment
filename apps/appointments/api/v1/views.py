from rest_framework import generics
from apps.appointments.models import Appointment
from .serializers import AppointmentSerializer

# Create and list appointments API view
class AppointmentListCreateAPIView(generics.ListCreateAPIView):
   
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

# Retrieve, Update and Delete API view
class AppointmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer