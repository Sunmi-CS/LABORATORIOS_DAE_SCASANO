from rest_framework import serializers
from .models import Quiz, Question, Choice

# Serializer para el modelo Quiz
# Los serializers en Django REST Framework convierten los objetos del modelo
# en formatos como JSON, para poder enviarlos o recibirlos desde una API.

class QuizSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'created_at']
    