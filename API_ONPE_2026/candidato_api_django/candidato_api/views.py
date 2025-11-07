# candidato_api/views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Candidate, NewsDetail, InvestigationDetail
from .serializers import CandidateSerializer, NewsDetailSerializer, InvestigationDetailSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(detail=True, methods=['get'])
    def news(self, request, pk=None):
        """Obtener noticias asociadas a un candidato"""
        candidate = self.get_object()
        news_docs = NewsDetail.objects.filter(
            related_candidate_name=candidate.name
        )
        serializer = NewsDetailSerializer(news_docs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def investigations(self, request, pk=None):
        """Obtener investigaciones asociadas a un candidato"""
        candidate = self.get_object()
        background = candidate.background_report
        if background and 'records' in background:
            investigation_ids = [
                record.get('documentId')
                for record in background['records']
            ]
            investigations = InvestigationDetail.objects.filter(
                document_id__in=investigation_ids
            )
            serializer = InvestigationDetailSerializer(investigations, many=True)
            return Response(serializer.data)
        return Response([])


class NewsDetailViewSet(viewsets.ModelViewSet):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'document_id'


class InvestigationDetailViewSet(viewsets.ModelViewSet):
    queryset = InvestigationDetail.objects.all()
    serializer_class = InvestigationDetailSerializer
    lookup_field = 'document_id'
