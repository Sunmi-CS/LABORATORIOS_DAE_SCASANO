# candidato_api/serializers.py

from rest_framework import serializers
from .models import Candidate, NewsDetail, InvestigationDetail


# 🧩 Serializador para los candidatos
class CandidateSerializer(serializers.ModelSerializer):
    # Campos JSON explícitos para que se serialicen correctamente
    academic_formation = serializers.JSONField()
    career_history = serializers.JSONField()
    background_report = serializers.JSONField()
    current_events = serializers.JSONField()

    class Meta:
        model = Candidate
        fields = [
            'id',
            'name',
            'party',
            'position',
            'photo_url',
            'basic_info',
            'asset_declaration',
            'government_plan',
            'academic_formation',
            'career_history',
            'background_report',
            'current_events'
        ]


# 🧩 Serializador para las noticias
class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail
        fields = '__all__'

    # Validación opcional para evitar duplicados de document_id
    def validate_document_id(self, value):
        if self.instance is None and NewsDetail.objects.filter(document_id=value).exists():
            raise serializers.ValidationError("Ya existe una noticia con este document_id.")
        return value


# 🧩 Serializador para las investigaciones
class InvestigationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigationDetail
        fields = '__all__'

    # Validación opcional similar
    def validate_document_id(self, value):
        if self.instance is None and InvestigationDetail.objects.filter(document_id=value).exists():
            raise serializers.ValidationError("Ya existe una investigación con este document_id.")
        return value


# 🧩 (Opcional) Serializador detallado: candidato + noticias + investigaciones
# Este no reemplaza al anterior, solo se usa si deseas devolver todo junto
class CandidateDetailSerializer(serializers.ModelSerializer):
    news = NewsDetailSerializer(many=True, read_only=True, source='get_related_news')
    investigations = InvestigationDetailSerializer(many=True, read_only=True, source='get_related_investigations')

    class Meta:
        model = Candidate
        fields = [
            'id',
            'name',
            'party',
            'position',
            'photo_url',
            'basic_info',
            'asset_declaration',
            'government_plan',
            'academic_formation',
            'career_history',
            'background_report',
            'current_events',
            'news',
            'investigations'
        ]
