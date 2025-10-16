from rest_framework import serializers
from .models import Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
    patients_count = serializers.IntegerField(source='patients.count', read_only=True)

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'created_at', 'patients_count']

class PatientSerializer(serializers.ModelSerializer):
    # Campo extra: mostrar el nombre del doctor en la respuesta (punto extra)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'diagnosis', 'doctor', 'doctor_name', 'created_at']
