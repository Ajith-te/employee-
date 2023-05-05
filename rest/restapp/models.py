from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=100)
    experience = models.FloatField()
    primary_skill = models.CharField(max_length=100)
    skills = models.JSONField(null=True)
    rating = models.FloatField()
    domains = models.CharField(max_length=100, null=True)
    last_insert = models.DateTimeField(default=timezone.now)
