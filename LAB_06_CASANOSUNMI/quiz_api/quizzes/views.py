from rest_framework import viewsets
from .models import Quiz
from .serializers import QuizDetailSerializer
 
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    