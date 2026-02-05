from rest_framework import serializers
from apps.appointments.models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ["id","customer_name","customer_email","appointment_datetime","status","notes","created_at"]
        read_only_fields = ["id", "created_at"]