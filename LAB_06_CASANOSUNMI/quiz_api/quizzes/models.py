from django.db import models

# - Creacion de Model Quiz
# - title: almacena el título del quiz 
# - description: permite una descripción opcional
# - created_at: guarda la fecha y hora en que se creó el registro
# El método __str__ devuelve el título del quiz 

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

