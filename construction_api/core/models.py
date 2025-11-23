# core/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Client(models.Model):
    """
    Клиент: физическое лицо или компания.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    is_company = models.BooleanField(default=False)
    company_details = models.TextField(blank=True, null=True)  # для юр. лиц

    def __str__(self):
        return self.name

class Project(models.Model):
    """
    Проект строительства. Связан с Client.
    """
    STATUS_CHOICES = [
        ('planned', 'Planned'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    address = models.CharField(max_length=512, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='planned')
    budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title

class Building(models.Model):
    """
    Конкретное здание/объект в рамках проекта (коттедж, таунхаус или многоэтажка).
    """
    BUILDING_TYPE = [
        ('cottage', 'Cottage'),
        ('townhouse', 'Townhouse'),
        ('apartment', 'Apartment Building'),
        ('office', 'Office Building'),
        ('other', 'Other'),
    ]
    project = models.ForeignKey(Project, related_name='buildings', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    building_type = models.CharField(max_length=30, choices=BUILDING_TYPE, default='other')
    floors = models.PositiveIntegerField(default=1)
    area_m2 = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.building_type})"

class Contractor(models.Model):
    """
    Подрядчик, работающий над проектом.
    """
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    projects = models.ManyToManyField(Project, related_name='contractors', blank=True)

    def __str__(self):
        return self.name
