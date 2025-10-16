from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Doctor, Patient
from .serializers import DoctorSerializer, PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'specialty']
    ordering_fields = ['name', 'created_at']

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.select_related('doctor').all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'diagnosis', 'doctor__name']
    ordering_fields = ['name', 'age', 'created_at']

    @action(detail=True, methods=['get'])
    def doctor_info(self, request, pk=None):
        patient = self.get_object()
        doctor = patient.doctor
        serializer = DoctorSerializer(doctor, context={'request': request})
        return Response(serializer.data)

