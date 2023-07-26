from django.db import models
import uuid


class TimeStample(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UUIDFY(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          unique=True,
                          editable=False)
    
    class Meta:
        abstract = True
