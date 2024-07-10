from django.db import models
from datetime import datetime
import uuid

class URL(models.Model):
    link = models.URLField(max_length=1000)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    short_uuid = models.CharField(max_length=5, unique=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.link

class UserAccess(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='accesses')
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    device = models.CharField(max_length=100, blank=True, null=True)
    time = models.DateTimeField(default=datetime.now)
    clicks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.ip_address} accessed {self.url.link}"
