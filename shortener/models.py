from datetime import datetime
import uuid
from django.db import models

class URL(models.Model):
    link = models.URLField(max_length=1000)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    short_uuid = models.CharField(max_length=5, unique=True)  # Add this field
    time = models.DateTimeField(default=datetime.now)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    device = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.link
