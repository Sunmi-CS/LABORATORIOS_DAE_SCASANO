# candidato_api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateViewSet, NewsDetailViewSet, InvestigationDetailViewSet

router = DefaultRouter()
router.register(r'candidatos', CandidateViewSet)
router.register(r'news', NewsDetailViewSet, basename='news')
router.register(r'investigations', InvestigationDetailViewSet, basename='investigations')

urlpatterns = [
    path('', include(router.urls)),
]
