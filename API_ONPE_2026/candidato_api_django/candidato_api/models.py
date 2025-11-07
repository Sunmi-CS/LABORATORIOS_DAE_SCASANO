# candidato_api/models.py

from django.db import models
from django.contrib.postgres.fields import ArrayField

class Candidate(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    party = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    photo_url = models.URLField()
    
    # Datos anidados (como JSON)
    basic_info = models.JSONField(default=dict)
    asset_declaration = models.JSONField(default=dict)
    government_plan = models.JSONField(default=dict)
    academic_formation = models.JSONField(default=dict)
    career_history = models.JSONField(default=dict)
    background_report = models.JSONField(default=dict)
    current_events = models.JSONField(default=dict)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return self.name

class NewsDetail(models.Model):
    document_id = models.CharField(max_length=100, unique=True, primary_key=True)
    title = models.CharField(max_length=500)
    summary = models.TextField()
    date = models.CharField(max_length=50)
    source = models.CharField(max_length=255)
    related_candidate_name = models.CharField(max_length=255)
    full_description = models.TextField()
    is_verified = models.BooleanField(default=False)
    image_url = models.URLField()
    source_url = models.URLField()
    
    def __str__(self):
        return self.title

class InvestigationDetail(models.Model):
    document_id = models.CharField(max_length=100, unique=True, primary_key=True)
    case_title = models.CharField(max_length=500)
    case_entity = models.CharField(max_length=255)
    case_date = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    timeline = models.JSONField(default=list)
    official_documents = models.JSONField(default=list)
    involved_parties = models.JSONField(default=list)
    
    def __str__(self):
        return self.case_title