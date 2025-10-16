from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=150)
    age = models.PositiveIntegerField(null=True, blank=True)
    diagnosis = models.TextField(blank=True)
    doctor = models.ForeignKey(Doctor, related_name='patients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.doctor.name})"
